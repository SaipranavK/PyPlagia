import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
import globals

from prep.splitter import BasketSep,TokenSep
from prep.verdict import verdict

from stringMatching.totalOccurences import TotalMatchCheck
from stringMatching.matchOccurences import OccurenceEquality
from stringMatching.custHammingDistance import HammingDistanceCheck

from stringMatching.synonymCheck import SynonymCheck

from styloMetric.prep import stylePrep
from styloMetric.checker import instrinsicCheck

metaInfo=[{'doc':'Pollution150.txt','author':'Alex Carry'},{'doc':'Pollution200.txt','author':'Emma White'},{'doc':'PollutionS2.txt','author':'Nate Wenmark'},{'doc':'School.txt','author':'Alex Carry'}]

#Preprocess and Store Candidate file
f1 = open('TestFiles/PollutionS2.txt','r')
temp1=''
LineSepX1=[]
WordSepX1=[]

globals.candidateName=f1.name

#store text in temp
for text in f1:
    temp1+=text
print("Raw")
print("-----------------------------------------------")
print(temp1)

#strip commas and brackets. Can be extended to other characters.
for line in temp1:   
    temp1=temp1.replace(',','')
    temp1=temp1.replace('(','')
    temp1=temp1.replace(')','')
    temp1=temp1.replace('\n','')


for key in temp1:
    if(key==''):
        temp1.remove(key)
        
print("\nProcessed")
print("-----------------------------------------------")
print(temp1)

BasketSep(LineSepX1,temp1)
print("\nLine Seperated list")
print("-----------------------------------------------")
print(LineSepX1)
print('\nNumber of  Lines: ',len(LineSepX1))

TokenSep(LineSepX1,WordSepX1)
print("\nWord Seperated list")
print("-----------------------------------------------")
print(WordSepX1)
print('\nNumber of  Words: ',len(WordSepX1))

f1.close()

#Preprocess and Store Comparision file
f1 = open('TestFiles/PollutionS2.txt','r')
temp1=''
LineSepX2=[]
WordSepX2=[]

globals.comparisionName=f1.name

#store text in temp
for text in f1:
    temp1+=text
print("Raw")
print("-----------------------------------------------")
print(temp1)

#strip commas and brackets. Can be extended to other characters.
for line in temp1:   
    temp1=temp1.replace(',','')
    temp1=temp1.replace('(','')
    temp1=temp1.replace(')','')
    temp1=temp1.replace('\n','')


for key in temp1:
    if(key==''):
        temp1.remove(key)
        
print("\nProcessed")
print("-----------------------------------------------")
print(temp1)

BasketSep(LineSepX2,temp1)
print("\nLine Seperated list")
print("-----------------------------------------------")
print(LineSepX2)
print('\nNumber of  Lines: ',len(LineSepX2))

TokenSep(LineSepX2,WordSepX2)
print("\nWord Seperated list")
print("-----------------------------------------------")
print(WordSepX2)
print('\nNumber of  Words: ',len(WordSepX2))

f1.close()

for info in metaInfo:
    candidateName=info['doc']
    stylePrep(metaInfo,candidateName)


#Total Matches
matchList=[]

for keyX1 in WordSepX1:
    for keyX2 in WordSepX2:
        if(keyX1 == keyX2 and keyX1 not in globals.grammarBox):
            if(keyX1 not in matchList):
                matchList.append(keyX1)
    
for i in range(0,len(matchList)):
    print('-----------------------------------------------')
    print("Word:",matchList[i])

from collections import Counter

X1_freq=dict(Counter(WordSepX1))
X2_freq=dict(Counter(WordSepX2))

matchCount=0

for key in matchList:
    matchCount+=X2_freq[key]
    
print("Match count=",matchCount)

#Checks
TotalMatchCheck(matchCount,WordSepX1)
OccurenceEquality(X1_freq,X2_freq)
HammingDistanceCheck(LineSepX1,LineSepX2)

instrinsicCheck(globals.plagFactor,metaInfo,candidateName,comparisionName)