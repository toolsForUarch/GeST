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

class DefaultFitness(object):
    '''
    classdocs
    '''

    '''
    Constructor
    '''
    def __init__(self):
        
        
        '''Override getFitness to specify other fitness functions  
        should be called after individual measurements are set (in other words the individual object instance at this point should carry the measurements with it)
        The getFitness function can be very sophisticated 
        e.g. take in account instruction count instruction mix, various metrics like perf counters power etc
        the getfitness should return an array where the first the first item MUST be the finess value, followed by any other useful information the user would like to see on file name of the indiviudal
        such as specific components ued to calculate the fitness and the individual measurements (like in the below example)
        To use the user defined fitness function specify the class name in the fitnessClass parameter in the configuration file
        '''
        
    def getFitness(self,individual): 
        fitness=individual.getMeasurements()[0]
        toReturn=[]
        toReturn.append(fitness)
        for value in individual.getMeasurements():
            toReturn.append(value)
        return toReturn