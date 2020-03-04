import globals
import sys

# Sytlometric Check
def instrinsicCheck(plagFactor,x,y,z):
    
    if(plagFactor>0.5):
        y=y.replace('TestFiles/','')
        z=z.replace('TestFiles/','')
        
        for info in x:
            if(info['doc']==y):
                CandidateAuthor=info['author']
                break
                
        for info in x:
            if(info['doc']==z):
                ComparisionAuthor=info['author']
                break

        print("Candidate Author - ",CandidateAuthor)
        print("Compared Author - ",ComparisionAuthor)
        
        candidateLineLength=0
        candidateEase=0
        comparedLineLength=0
        comparedEase=0
        
        for author in authorMeta:
            if(author['author']==CandidateAuthor):
                candidateLineLength=author['avgLineLength']
                candidateEase=author['Ease']
            elif(author['author']==ComparisionAuthor):
                comparedLineLength=author['avgLineLength']
                comparedEase=author['Ease']
                
        if(candidateLineLength>=comparedLineLength*0.7):
            if(candidateEase>=comparedEase*0.7):
                print("Suspicious Document")
            else:
                print("plagiarised")
        else:
            print("inconclusive")
            
    else:
        print("Not plagiarised")

    sys.exit()