from globals import *

#null preprocessing
def cleaner(x):
    for key in x:
        if(key=="" or key==" "):
            x.remove(key)
            
#split temp1 parsing individual lines stored as a string into x.
def BasketSep(x,temp1):
    startpoint=0
    for char in range(0,len(temp1)):
        if(temp1[char]=='.'):
            store=temp1[startpoint:char]
            x.append(store)
            startpoint=char+1
    
    cleaner(x)

#split x parsing individual words stored as a string into y.
def TokenSep(x,y):
    KeyStart=0
    for index in range(0,len(x)):
        tempdump=x[index]
        for char in range(0,len(tempdump)):
            if(tempdump[char]==' '):
                store=tempdump[KeyStart:char]
                y.append(store)
                KeyStart=char+1
            elif(char==len(tempdump)-1):
                store=tempdump[KeyStart:char+1]
                y.append(store)
                KeyStart=char+1
                
    cleaner(y)
