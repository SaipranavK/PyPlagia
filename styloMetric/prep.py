import globals
import textstat
from prep.splitter import BasketSep,TokenSep
# Sytlometric Evaluator
def stylePrep(x,y):

    LineSeptemp=[]
    LineSep=[]
    WordSeptemp=[]
    WordSep=[]
    author=''
    docMeta=[]
    authorBooks=[]
        
    for info in x:
        if(info['doc']==y):
            author=info['author']
            break
            
    if(author not in globals.valuatedList):
        
        print("===========================================================================")
        print("\nAuthor - ",author)
        
        for info in x:
            if(info['author']==author):
                authorBooks.append(info['doc'])

        print("Docs by ",author," - ",authorBooks)

        for book in authorBooks:
            del LineSeptemp[:]
            del WordSeptemp[:]

            f1=open('TestFiles/'+book,'r')
            temp1=''

            #store text in temp
            for text in f1:
                temp1+=text

            #strip commas and brackets. Can be extended to other characters.
            for line in temp1:   
                temp1=temp1.replace(',','')
                temp1=temp1.replace('(','')
                temp1=temp1.replace(')','')
                temp1=temp1.replace('\n','')


            for key in temp1:
                if(key==''):
                    temp1.remove(key)

            BasketSep(LineSeptemp,temp1)
            TokenSep(LineSeptemp,WordSeptemp)

            for line in LineSeptemp:
                LineSep.append(line)

            for word in WordSeptemp:
                WordSep.append(word)

            metaBlock=[{'doc':f1.name,'lines':len(LineSeptemp),'words':len(WordSeptemp)}]

            docMeta.append(metaBlock)

        print('\nDocs Data')
        print('-----------------------------------------')
        print(docMeta)

        print('\nAuthor Insigth')
        print('-----------------------------------------')
        avgLineLenght=len(WordSep)/len(LineSep)
        print("Average Line Length: ",avgLineLenght)


        vocab=[]
        for word in WordSep:
            if(word not in globals.grammarBox):
                vocab.append(word)

        totalEase=0

        for line in LineSep:
            totalEase+=textstat.flesch_reading_ease(line)

        avgEase=totalEase/len(LineSep)

        print("Ease of reading: ",avgEase)

        authorIns={'author':author,'avgLineLength':avgLineLenght,'Ease':avgEase}
        globals.authorMeta.append(authorIns)
        
        globals.valuatedList.append(author)

