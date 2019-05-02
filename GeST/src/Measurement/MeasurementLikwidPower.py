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

from Measurement.Measurement import Measurement

class MeasurementLikwidPower(Measurement):
    '''
    classdocs
    '''
    
    def __init__(self,confFile):
        super().__init__(confFile)
     
    
    def init(self):
        super().init()
        self.timeToMeasure = self.tryGetIntValue('time_to_measure')
    
    #the below code is tested to work with likwid 4.3 and 3.1 versions
    
    def measure(self):  
            
        super().copyFileOverFTP()
        compilation_command="cd "+self.targetRunDir + " ; gcc main.s -o individual &>/dev/null;"
        execution_command="cd "+self.targetRunDir+" ; "
        for core in self.coresToUse:
                execution_command+="taskset -c "+str(core)+" ./individual  &>/dev/null &  "
        execution_command+=" sudo likwid-powermeter  -s "+str(self.timeToMeasure) +"s > tmp ; pkill individual &> /dev/null;" #make sure that msr module is loaded (modprobe msr) and sudo without password is enabled
        output_command="cd "+self.targetRunDir + " ; cat tmp | grep Watt | head -n 1 | awk '{print $3}'; rm main.s; rm individual; rm tmp; "; #this grabs the package power
        super().executeSSHcommand(compilation_command)
        super().executeSSHcommand(execution_command)
        stdout=super().executeSSHcommand(output_command)
                     
        
        for line in stdout:
            try:
                test=float(line)
                power_meas=test
            except ValueError:
                print ("Exception line not power")
   

        measurements=[];
        measurements.append(power_meas);
        
        return measurements;
            