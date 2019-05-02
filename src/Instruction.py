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
import copy
import sys;


class Instruction(object):
    '''
    classdocs
    '''


    def __init__(self,name,ins_type,numOfOperands,operands=[],format="op1,op2,op3",toggleable="False"):
        '''
        Constructor
        '''
        self.name = name;
        self.ins_type = ins_type;
        self.operands = operands;
        self.format=format;
        self.format=self.format.replace("\\n","\n"); #replace double backslashes with one backslash to make sure atomic sequences work. for some reason the xml parsing by default ads a backslash to escape characters
        self.format=self.format.replace("\\t","\t");
        self.numOfOperands = numOfOperands;
        self.toggleable=toggleable;
        
    def copy(self):
        return copy.deepcopy(self);
            
        
    def setOperands (self,operands):
        self.operands=operands;
        
    def getOperand(self,index=0):
        if (index>=self.operands.__len__() or index <0):
            print("error index out of bounds")
            sys.exit;
        return self.operands[index];
    
    def getOperands(self):
        return self.operands;
    
    def toggle(self,value_index): #It's the algorithm class job to provide the right indexes for toggling
        for op in self.operands:
                if(op.toggleable=="True"):
                    op.setCurrentValueByIndex(value_index);
                      
        
    def mutateOperands (self,rand):##TODO maybe give an option of changing particular operands
        for op in self.operands:
            op.mutate(rand);
            
    ''' def toggle(self): #TODO think if you really need this
       '''
           
        
    def __str__ (self):
        
        if( (str(self.numOfOperands).strip() == "0") or (self.operands[0].currentValue!= "") ):
            representation=self.format
            for i in range(0,self.operands.__len__()):
                toReplace="op"+str(i+1);
                representation=representation.replace(toReplace.__str__(),str(self.operands[i].__str__()));

            #representation=self.name + " " + representation
            return representation
        else:
            representation="name "+self.name + "\ntype "+self.ins_type +"\nformat "+self.format+"\nnumOfOperands "+self.numOfOperands+"\n";
            for i in range(int(self.numOfOperands)):
                representation+=("\t"+str(self.operands[i])+"\n");
            return representation;

