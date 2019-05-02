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
import sys
class Operand(object):  
    '''
    classdocs
    '''
    

    def __init__(self,id,type,values=[],min=0,max=4294967296,stride=1,toggleable="False"): 
        '''Constructor takes as parameters the values an operand can take either in array or in bounds format'''
        self.values = values;
        self.min = min;
        self.max = max;
        self.stride = stride;
        self.currentValue="";
        self.id=id;
        self.type=type;
        self.toggleable=toggleable
        if( (int(min)>int(max)) or (int(stride)<=0)):
            print("Watch out you should always put a stride above 0 otherwise an infinitive loop will be caused and min should be less or equal than max");
            sys.exit();
        if not self.values: #if possible values not set.. manually create them
            if(self.type!="automatically_incremented_operand"): #some types are automatically implemented e.g. branch labels
                i=int(self.min);
                while(i<=int(self.max)):
                    self.values.append(i);
                    i+=int(self.stride);      
        #self.togleValue=self.values[0];
             
    def copy(self):
        return copy.deepcopy(self);
    
    def mutate(self,rand):
        '''Basicaly sets as current value a random value from the acceptable range'''
        if(self.type=="automatically_incremented_operand"):
            self.currentValue=self.min;
        else:    
            self.currentValue=rand.choice(self.values);
        
        
    def getValue(self):
        return self.currentValue;
    
    def setCurrentValueByIndex(self,index):
        self.currentValue=self.values[index];
    
    '''def toggle(self): 
        if(self.toggleable=="True"): 
            if(self.togleValue==self.values[0]):
                self.togleValue=self.values[1];
            else:
                self.togleValue=self.values[0];
                
        def setToggleValueAsCurrent(self):
        if(self.toggleable=="True"):
            self.currentValue=self.togleValue;'''
    
    def __str__(self):
        if(self.currentValue != ""):
            return str(self.currentValue);
        else:
            return str(self.id);

