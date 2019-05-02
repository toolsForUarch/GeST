'''
Copyright 2019 ARM Ltd. and University of Cyprus
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from abc import ABC, abstractmethod
from xml.dom import minidom
from paramiko import SSHClient, client
import paramiko
import socket
import platform
import visa
import os

class Measurement(ABC):
    '''
    classdocs
    '''

    def __init__(self, confFile):
        '''
        Constructor
        '''
        self.confFile=confFile
        self.xmldoc = minidom.parse(confFile)
        
        #most of the below are expected to be initialized in init function (should be called after constructor)
        self.targetRunDir= None
        self.targetHostname= None
        self.targetSSHusername= None
        self.targetSSHpassword = None
        self.coresToUse=None
        self.sourceFilePath=None #to be set in setSourceFilePath funtion
        super().__init__() #abstract class init
        
    def init(self): #should be called after constructor.. this can be overridden by child measurement classes to add new or use other configuration parameters..

        self.targetRunDir= self.tryGetStringValue('targetRunDir')
        self.targetHostname= self.tryGetStringValue('targetHostname')
        self.targetSSHusername= self.tryGetStringValue('targetSSHusername')
        self.targetSSHpassword = self.tryGetStringValue('targetSSHpassword')
        coresToUseString=self.tryGetStringValue('coresToUse')
        self.coresToUse=[]
        for core in coresToUseString.split(" "):
            self.coresToUse.append(int(core))
    
    def setSourceFilePath(self,sourceFilePath): #should be called before measurement or in the begining of the GA run if the source file path doesn't changes
        self.sourceFilePath=sourceFilePath
        
    ##helper functions to make clearer the code.. on exception the code doesn't terminate immediately but it does produce a warning message.. 
    ##This is the case because sometimes this might be desirable based on the functionality.. For instance bare metal runs won't use the ssh parameters 
    def tryGetStringValue(self,key):
        try:
            value=self.xmldoc.getElementsByTagName(key)[0].attributes['value'].value;
            return value
        except:
            print("Warning failed to read "+str(key))
        
    def tryGetIntValue(self,key):
        try:
            value=int(self.xmldoc.getElementsByTagName(key)[0].attributes['value'].value);
            return value
        except:
            print("Warning failed to read "+str(key))
    
    def tryGetFloatValue(self,key):
        try:
            value=float(self.xmldoc.getElementsByTagName(key)[0].attributes['value'].value);
            return value
        except:
            print("Warning failed to read "+str(key))
        
    #this function should return an array of results.. at least one item should be returned.. the defaultFitness.py class (that calculates indidual's fitness) assumes by convention that the first array
    #item is the fitness value 
    @abstractmethod
    def measure(self): 
        pass
    
    ## utility function for executing commands over ssh connection.. very common functionality
    def executeSSHcommand(self,command,continousAttempt=True,max_tries=10):
        tries=0
        while True:
            try:
                ssh = SSHClient()
                ssh.set_missing_host_key_policy(client.AutoAddPolicy()) 
                ssh.connect(self.targetHostname, username=self.targetSSHusername, password=self.targetSSHpassword)
                stdin,stdout,stderr =ssh.exec_command(command)
                lines=[]
                for line in stdout.readlines():
                    lines.append(line)
                ssh.close()
                return lines
                
            except:
                if continousAttempt and tries<max_tries:
                    tries=tries+1
                    continue
                else:
                    raise("Exception: Unable to execute command "+str(command))
    
    def executeSSHcommandNonBlocking(self,command,continousAttempt=True,max_tries=10):
        tries=0
        while True:
            try:
                ssh = SSHClient()
                ssh.set_missing_host_key_policy(client.AutoAddPolicy()) 
                ssh.connect(self.targetHostname, username=self.targetSSHusername, password=self.targetSSHpassword)
                ssh.exec_command(command)
                ssh.close()
                return
            except:
                if continousAttempt and tries<max_tries:
                    tries=tries+1
                    continue
                else:
                    raise("Exception: Unable to execute command "+str(command))
                
    #### utility function for copying the source file over ssh connection.. very common functionality        
    def copyFileOverFTP(self,continousAttempt=True):
        while True:
            try:
                ssh = SSHClient()
                ssh.set_missing_host_key_policy(client.AutoAddPolicy()) 
                ssh.connect(self.targetHostname, username=self.targetSSHusername, password=self.targetSSHpassword)
                sftp=ssh.open_sftp();
                sftp.put(self.sourceFilePath,self.targetRunDir+"/main.s")
                sftp.close()
                ssh.close()
                break    
            except:
                if continousAttempt:
                    continue
                else:
                    raise("Exception: Unable to copy file")
        
        
    def ping (self,host):
        """
        Returns True if host responds to a ping request
        """
        # Ping parameters as function of OS
        ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
        
        # Ping
        return os.system("ping " + ping_str + " " + host) == 0  
            
    
    