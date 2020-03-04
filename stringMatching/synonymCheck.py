import globals

#synonym check using wordNET
def SynonymCheck(x,y):
    synMatch=0
    synonymns=[]
    w1=[]
    w2=[]
    
    for i in x:
        w1.append(i)
        
    for i in y:
        w2.append(i)
    
    for i in w1:
        del synonymns[:]
        for syn in wordnet.synsets(i):
            for l in syn.lemmas():
                synonymns.append(l.name())
        for j in w2:
            for instance1 in synonymns:
                    if(instance1==j):   
                        synMatch+=1
    synMatch=(synMatch/len(x))
    return synMatch