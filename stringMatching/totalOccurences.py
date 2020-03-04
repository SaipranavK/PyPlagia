import globals
from prep.verdict import verdict

#count total occurences    
def TotalMatchCheck(x,y):
    temp=[]    

    for key in y:
        if(key not in globals.grammarBox):
            temp.append(key)

    globals.plagFactor=x/(len(temp))
    print("globals.plagFactor after TotalMatchCheck=",globals.plagFactor)
    if(globals.plagFactor>=0.75):
        res=1
    else:
        res=0
        
    verdict(res,globals.plagFactor)