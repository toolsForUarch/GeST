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
import os
import sys
import pickle
import pprint;
from Population import Population
from Individual import Individual
from Instruction import Instruction
from Operand import Operand
import re;


path = sys.argv[1] 
files=[]
for root, dirs, filenames in os.walk(path): #takes as input the dir with the saved state
    for f in filenames:
        if((".pkl" in f) and ("rand" not in f)):
            files.append(f);

files.sort(key=lambda x:  int(x.split('.')[0]));
pop=Population([]);
allValues="";
allKeys="";
columns=[];
theBest=[];
print("best and average of each generation");
print("generation best average");
insHash={};

for f in files:
    input=open(path+f,"rb");
    pop=pickle.load(input);
    input.close();
    columns.append(f.split('.')[0]);
    best=pop.getFittest();
    theBest.append(best);
    sum=0.0;
    count=0;
    for indiv in pop.individuals:
        sum+=float(indiv.getFitness());
        count+=1;
        for ins in indiv.sequence:
            
                if(ins.name in insHash.keys()):
                    insHash[ins.name]+=1;
                else:
                    insHash[ins.name]=1;
    sorted(insHash,key=lambda key: insHash[key]);
    #print(insHash);
    allKeys+=list(insHash.keys()).__str__()+"\n";
    allValues+=insHash.values().__str__()+"\n";
    average=sum/count;
    for key in list(insHash.keys()): #clear the hash for the next population
        insHash[key]=0;
    
    print(str(columns[-1])+" "+str(round(float(best.getFitness()),6))+" "+str(round(float(average),6))  );
#print (allKeys);
print("end of generation best average");

values=re.sub("[A-Za-z]", "", allValues);
values=re.sub("[\[\]\(\),_]", "", values);
values=values.strip(' \n');
data=[];
totalSize=pop.individuals[0].getInstructions().__len__()*pop.getSize();
#print (values);
for row in values.split("\n"):
    #print(row);
    data.append([float(float(s)/float(totalSize)) for s in row.split()])
    #data.append([int(s) for s in row.split()])
#data=pprint.pformat (data);


rows=re.sub("[\[,\'\]]", "", allKeys);
rows=re.sub("[\{\}\':,]", "", rows);
rows=rows.strip(' \n');

for column in rows.split("\n"):
    #print(row);
    rows=[str(s) for s in column.split()]


print("Instruction Mix per generation");

print (" "+' '.join(rows));

for i in range(columns.__len__()):
    print (columns[i],end=" ");
    for j in range(rows.__len__()):
        print(round(data[i][j],2),end=" ");
    print("");
    
#print(values);

print("Instruction Mix for best of each generation");

print (" "+' '.join(rows));


loopSize=theBest[0].getInstructions().__len__()

i=1;
for indiv in theBest:
    for key in list(insHash.keys()): #clear the hash for the next individual
        insHash[key]=0;
    for ins in indiv.sequence:
                if(ins.name in insHash.keys()):
                    insHash[ins.name]+=1;
                else:
                    insHash[ins.name]=1;
    sorted(insHash,key=lambda key: insHash[key]);
    print(str(i),end=" ");
    i+=1;
    for key in list(insHash.keys()):
        print(round(float(float(insHash[key])/loopSize),2),end=" ");
    print("");

print("Type Mix for best of each generation");

typeHash={};

i=1;
for indiv in theBest:
    for key in list(typeHash.keys()): #clear the hash for the next individual
        typeHash[key]=0;
    for ins in indiv.sequence:
                try:
                    if(ins.type in typeHash.keys()):
                        typeHash[ins.type]+=1;
                    else:
                        typeHash[ins.type]=1;
                except: #in legacy pkls the attribute was type instead of ins_type
                    if(ins.ins_type in typeHash.keys()):
                        typeHash[ins.ins_type]+=1;
                    else:
                        typeHash[ins.ins_type]=1;
                    
    sorted(typeHash,key=lambda key: typeHash[key]);
    print(str(i),end=" ");
    i+=1;
    for key in list(typeHash.keys()):
        print(round(float(float(typeHash[key])/loopSize),2),end=" ");
    print("");
for key in typeHash.keys():
    print(key,end=" ")

sys.exit();

