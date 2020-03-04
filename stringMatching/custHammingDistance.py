import globals
from prep.splitter import BasketSep,TokenSep
from stringMatching.longestSubString import LongestSubString
from prep.verdict import verdict

#match occurences in basket
def HammingDistanceCheck(x,y):
    LineX1=[]
    LineX2=[]
    tempX1=[]
    tempX2=[]
    uniqueSetX1=[]
    uniqueSetX2=[]
    
    for lineX1 in x:
        del tempX1[:]
        del LineX1[:]
        del uniqueSetX1[:]
        tempX1.append(lineX1)
        TokenSep(tempX1,LineX1)
        
        for lineX2 in y:
            HammMatch=0
            del tempX2[:]
            del LineX2[:]
            del uniqueSetX2[:]
            tempX2.append(lineX2)
            TokenSep(tempX2,LineX2)
            
            LongestSubString(LineX1,lineX2,LineX2,x)
                
            if(len(LineX1)==len(LineX2) or len(LineX1)==(len(LineX2))+1 or (len(LineX1))+1==len(LineX2) or len(LineX1)==(len(LineX2))+2 or (len(LineX1))+2==len(LineX2) or len(LineX1)==(len(LineX2))-1 or (len(LineX1))-1==len(LineX2) or len(LineX1)==(len(LineX2))-2 or (len(LineX1))-2==len(LineX2)):
                
                for keyX1 in LineX1:
                    for keyX2 in LineX2:
                        if(keyX1==keyX2 and keyX1 not in globals.grammarBox):
                            HammMatch+=1
                
                if((HammMatch/len(LineX1))>=0.30):
                    for keyX1 in LineX1:
                        for keyX2 in LineX2:
                            if(keyX1!=keyX2 and keyX1 not in grammarBox and keyX2 not in grammarBox and keyX1 not in uniqueSetX1 and keyX2 not in uniqueSetX2):
                                uniqueSetX1.append(keyX1)
                                uniqueSetX2.append(keyX2)
                                
                    synMatch=SynonymCheck(uniqueSetX1,uniqueSetX2)
                    if((synMatch/len(LineX1))>=0.40):
                        globals.plagFactor+=(((HammMatch+synMatch)/len(LineX1))/(len(x)))
                        
                    else:
                        globals.plagFactor+=((HammMatch/len(LineX1))/(len(x)))
                                
                    
    print("globals.plagFactor after HammingDistCheck=",globals.plagFactor)
    if(globals.plagFactor>=0.75):
        res=1
    else:
        res=0
          
    verdict(res,globals.plagFactor)