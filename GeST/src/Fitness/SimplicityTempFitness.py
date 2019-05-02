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

class SimplicityTempFitness(object): # a fitness function for maximizing both temperature and instruction stream simplicity
    '''
    classdocs
    '''
    
    '''
    Constructor
    '''
    def __init__(self):
        self.MAX_TEMP=100
        self.BASELINE_TEMP=40
        self.MAX_TEMP_SCORE=self.MAX_TEMP-self.BASELINE_TEMP
        self.percentages=[0.5,0.5]
    
        
        '''Override this function to specify other fitness functions  
        should be called after individual measurements are set (in other words the individual object instance at this point should carry the measurements with it)
        The getFitness function can be very sophisticated 
        e.g. take in account instruction count instruction mix, various metrics like perf counters power etc
        the getfitness should return an array where the first the first item MUST be the finess value, followed by any other useful information the user would like to see on file name of the indiviudal
        such as specific components ued to calculate the fitness and the individual measurements (like in the below example)
        To use the user defined fitness function specify the class name in the fitnessClass parameter in the configuration file
        '''
        
    def getFitness(self,individual): 
        insHash={}
        instructions=individual.getInstructions()
        totalInstructions=len(instructions)
        
        for ins in instructions:
            insHash[ins.name]=1
        uniqueIns=len(insHash.keys())
        
        tempScore=(individual.getMeasurements()[0]-self.BASELINE_TEMP) / self.MAX_TEMP_SCORE
        tempScoreWeighted=tempScore*self.percentages[0]
        
        instructionsScore=(totalInstructions - uniqueIns)/totalInstructions
        instructionsScoreWeighted=instructionsScore*self.percentages[1]
        
        fitness=tempScoreWeighted+instructionsScoreWeighted 
        
        toReturn=[]
        toReturn.append(fitness)
        toReturn.append(tempScoreWeighted)
        toReturn.append(instructionsScoreWeighted)
        for value in individual.getMeasurements():
            toReturn.append(value)
        return  toReturn