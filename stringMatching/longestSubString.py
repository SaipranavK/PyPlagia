import globals
from prep.verdict import verdict

def LongestSubString(x,y,z,a):
    appString=x[0]
    subCount=0
    uniqueSetX1=[]
    uniqueSetX2=[]

    for instance in range(1,len(x)):
        result=y.find(appString)
        if(result!=-1):
            subCount+=1
            appString+=" "+x[instance]
        else:
            appString=x[instance]
    
    subCount+=1
    if((subCount/len(x))>0.60):
        
        for keyX1 in x:
            for keyX2 in z:
                if(keyX1!=keyX2 and keyX1 not in grammarBox and keyX2 not in grammarBox and keyX1 not in uniqueSetX1 and keyX2 not in uniqueSetX2):
                    uniqueSetX1.append(keyX1)
                    uniqueSetX2.append(keyX2)
                    
        synMatch=SynonymCheck(uniqueSetX1,uniqueSetX2)
        
        if((synMatch/len(x))>=0.40):
            globals.plagFactor+=(((subCount+synMatch)/len(x))/(len(a)))
                        
        else:
            globals.plagFactor+=((subCount/len(x))/(len(a)))
