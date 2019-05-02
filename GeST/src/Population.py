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

import operator
import pickle

class Population(object):
    '''
    classdocs
    '''


    def __init__(self,individuals=[]):
        self.individuals=individuals;
        
    
    def getIndividual(self,index):
        return self.individuals[index];
        
    def getFittest(self):
        best_value=float(self.individuals[0].getFitness());
        best_indiv=self.individuals[0];
        for i in range (self.individuals.__len__()):
            if float(self.individuals[i].getFitness()) > best_value:
                best_value=float(self.individuals[i].getFitness()) 
                best_indiv=self.individuals[i];        
        return best_indiv;
    
    def getAvgFitness(self):
        sum=0
        for indiv in self.individuals:
            sum+=float(indiv.getFitness())
        avg=sum/self.individuals.__len__()
        return avg
    def getSize (self):
        return self.individuals.__len__()
    
    def pickRandomlyAnIndividual(self,rand):
        return rand.choice(self.individuals);
        
    def setCumulativeFitness(self): #for roulette wheel selection
        sum=0.0;
        self.individuals[0].setCumulativeFitness(int(self.individuals[0].getFitness()*1000000));
        for i in range(1,self.individuals.__len__()):
            fitness=int(self.individuals[i].getFitness()*1000000);
            self.individuals[i].setCumulativeFitness(self.individuals[i-1].cumulativeFitness+fitness);
                    
    def sortByFitessToWeakest(self):
        self.individuals.sort(key=operator.attrgetter('fitness'),reverse=True)
        
    def sortByWeakestToFitess(self):
        self.individuals.sort(key=operator.attrgetter('fitness'))
        #sorted(self.individuals,key=lambda obj: obj.fitness, reverse=True);
    
    def saveIndividual (self,index,individual):
        self.individuals[index]=individual;
        
    def __str__(self):
        output="";
        for code in self.individuals:
            output+=str(code.__str__()+"\n");
        return output;
    
    def keepHalfBest(self):
        self.sortByFitessToWeakest();
        half=int(self.individuals.__len__()/2);
        newList=[]
        for i in range(0,half):
            newList.append(self.individuals[i]);
        self.individuals=newList;
        
        
    def pickle(self,filename):
        pickle.dump(self, filename);
        
    @staticmethod
    def unpickle(filename):
        return pickle.load(filename);