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
import pickle;
import copy;

class Individual(object):
    '''
    classdocs
    '''
    id=0;

    def __init__(self,sequence=[],generation=0): #Note This code assumes that instruction operands are initiated (mutated) from before
        Individual.id+=1;
        self.myId=Individual.id;
        self.sequence=sequence;
        self.fitness=0.0; 
        #self.secondaryMeasurement=0.0;
        self.measurements=[]
        self.branchLabels={};
        self.cumulativeFitness=0.0; #for wheel selection
        self.parents=[];
        self.generation=generation;
        self.fixUnconditionalBranchLabels();
        return;
    
    def addInstruction(self,anInstruction):
        self.sequence.append(anInstruction);
    
    def getInstruction(self,index):
        return self.sequence[index];
    
    def getInstructions(self):
        return self.sequence;
    
    def fixUnconditionalBranchLabels(self):
        automatically_incremented={};
        for ins in self.sequence:
            for operand in ins.getOperands():
                if(operand.type=="automatically_incremented_operand"): 
                    if(operand.id in automatically_incremented.keys()):
                        automatically_incremented[operand.id]+=int(operand.stride);
                    else:
                        automatically_incremented[operand.id]=int(operand.min);
                    operand.currentValue=automatically_incremented[operand.id];
    
    def setMeasurementsVector(self,measurements):#by convention the first item of the vector is the fitness value
        self.measurements=measurements
    
    def setFitness(self,fitness):
        self.fitness=fitness
    
    '''def setMeasurementsVector(self,measurements): 
        self.measurements=measurements
        return;'''
    
    def setCumulativeFitness(self,fitness): #for wheel selection
        self.cumulativeFitness=fitness;
    
    def getFitness(self):
        try:
            return self.fitness; #by convention the first item of the vector is the fitness value
        except:
            return self.measurement #to support continuing runs from legacy population pkls
    #def getSecondaryMeasurement(self):
    #    return self.secondaryMeasurement;
    def getMeasurements(self):
        return self.measurements
    
    def setParents(self,par1,par2): ##the first parent is the code that remains the same.. the second parent is the code that came after crossover
        self.parents.append(par1);
        self.parents.append(par2);
    
    def clearParents(self):
        self.parents=None;
    
    def belongsToInitialSeed(self):
        if self.parents:
            return False;
        else:
            return True;
        
    def __str__(self):
        index=0;
        output=""
        for ins in self.sequence:
            output+=str("\t"+ins.__str__()+"\n");
            if str(index) in self.branchLabels.keys():
                output+=str(self.branchLabels[str(index)]+"\n");
            index+=1;
        return output;
    
    def __cmp__(self,other):
        if self.getFitness()  < other.getFitness():
            return -1
        elif self.getFitness()> other.getFitness():
            return 1
        else:
            return 0
        
    def pickle(self,filename):
        pickle.dump(self, filename);
    
    @staticmethod
    def unpickle(filename):
        return pickle.load(filename);
    
    def copy(self):
        return copy.deepcopy(self);
    