import globals
from prep.verdict import verdict

# match occurences 
def OccurenceEquality(x,y):
    occCount=0

    for keyX1 in x:
        occCount+=x[keyX1]
        
    for keyX1 in x:
        for keyX2 in y:
            if(keyX1==keyX2):
                if(x[keyX1]==y[keyX2]):
                    globals.plagFactor+=x[keyX1]/occCount

    print("globals.plagFactor after OccurenceEquality=",globals.plagFactor)
    if(globals.plagFactor>=0.75):
        res=1
    else:
        res=0
        
    verdict(res,globals.plagFactor)