import re, pprint, itertools, ast, random

firstString = input('Type the words that you want to be rhymed: ')

splitList = firstString.split(' ')

#print(splitList)

#testString = input('Type a word')

rhymesList = []

def rhymeSwap(searchString):

    searchStringUp = searchString.upper()

    subRegex = re.compile(r'\d')

    prettyRegex = re.compile(r'\(\d\)')

    stripPattern4 = r'\w*\d? \w*\d? \w*\d? \w*\d?$'
    stripPattern3 = r'\w*\d? \w*\d? \w*\d?$'
    stripPattern2 = r'\w*\d? \w*\d?$'
    stripPattern1 = r'\w*\d?$'

    tempRegex4 = re.compile(stripPattern4)
    tempRegex3 = re.compile(stripPattern3)
    tempRegex2 = re.compile(stripPattern2)
    tempRegex1 = re.compile(stripPattern1)
    
    wordPronDictFile = open('/Users/johnglennvoorhess/Documents/wordPronDictFile.txt', 'r')
    wordPronDict = wordPronDictFile.read()
    wordPronDict = ast.literal_eval(wordPronDict)
    wordPronDictFile.close()

    pronWordDict4File = open('/Users/johnglennvoorhess/Documents/pronWordDict4File.txt', 'r')
    pronWordDict4 = pronWordDict4File.read()
    pronWordDict4 = ast.literal_eval(pronWordDict4)
    pronWordDict4File.close()

    pronWordDict3File = open('/Users/johnglennvoorhess/Documents/pronWordDict3File.txt', 'r')
    pronWordDict3 = pronWordDict3File.read()
    pronWordDict3 = ast.literal_eval(pronWordDict3)
    pronWordDict3File.close()

    pronWordDict2File = open('/Users/johnglennvoorhess/Documents/pronWordDict2File.txt', 'r')
    pronWordDict2 = pronWordDict2File.read()
    pronWordDict2 = ast.literal_eval(pronWordDict2)
    pronWordDict2File.close()

    pronWordDict1File = open('/Users/johnglennvoorhess/Documents/pronWordDict4File.txt', 'r')
    pronWordDict1 = pronWordDict1File.read()
    pronWordDict1 = ast.literal_eval(pronWordDict1)
    pronWordDict1File.close()

    if searchStringUp in wordPronDict.keys():
#        print('In Dict')
        searchPron = wordPronDict[searchStringUp]

        mo4StringUnstressed = ''
        mo3StringUnstressed = ''
        mo2StringUnstressed = ''
        mo1StringUnstressed = ''


        if tempRegex4.search(searchPron) != None:
            mo4String = str(tempRegex4.search(searchPron).group())
            mo4StringUnstressed = subRegex.sub('', mo4String)

        if tempRegex3.search(searchPron) != None:
            mo3String = str(tempRegex3.search(searchPron).group())
            mo3StringUnstressed = subRegex.sub('', mo3String)
        
        if tempRegex2.search(searchPron) != None:
            mo2String = str(tempRegex2.search(searchPron).group())
            mo2StringUnstressed = subRegex.sub('', mo2String)

        if tempRegex4.search(searchPron) != None:
            mo1String = str(tempRegex1.search(searchPron).group())
            mo1StringUnstressed = subRegex.sub('', mo1String)

        rhymeListBig = list()
        
        if mo4StringUnstressed in pronWordDict4.keys() and len(pronWordDict4.get(mo4StringUnstressed,0)) > 1:
            rhymeList4 = pronWordDict4[mo4StringUnstressed]
            del rhymeList4[rhymeList4.index(searchStringUp)]
            for i in range(len(rhymeList4)):
                rhymeListBig.append(rhymeList4[i])

        if mo3StringUnstressed in pronWordDict3.keys() and len(pronWordDict3.get(mo3StringUnstressed,0)) > 1:
            rhymeList3 = pronWordDict3[mo3StringUnstressed]
            del rhymeList3[rhymeList3.index(searchStringUp)]
            for i in range(len(rhymeList3)):
                rhymeListBig.append(rhymeList3[i])

        if mo2StringUnstressed in pronWordDict2.keys() and len(pronWordDict2.get(mo2StringUnstressed,0)) > 1:
            rhymeList2 = pronWordDict2[mo2StringUnstressed]
            del rhymeList2[rhymeList2.index(searchStringUp)]
            for i in range(len(rhymeList2)):
                rhymeListBig.append(rhymeList2[i])
#            randomRhyme = prettyRegex.sub('', randomRhyme)
#            randomRhyme = random.choice(rhymeList2)
#            print(randomRhyme)

        elif mo1StringUnstressed in pronWordDict1.keys() and len(pronWordDict1.get(mo1StringUnstressed,0)) > 1:
            rhymeList1 = pronWordDict1[mo1StringUnstressed]
            del rhymeList1[rhymeList1.index(searchStringUp)]
            for i in range(len(rhymeList1)):
                rhymeListBig.append(rhymeList1[i])
            randomRhyme = random.choice(rhymeList1)
            randomRhyme = prettyRegex.sub('', randomRhyme)
#            print(rhymeList1)
#            print(randomRhyme)
            rhymesList.append(randomRhyme)
        else:
            print('huh')

        if len(rhymeListBig) > 1:
#            print(rhymeListBig)
            randomRhyme = random.choice(rhymeListBig)
            randomRhyme = prettyRegex.sub('', randomRhyme)
#            print(randomRhyme)
            rhymesList.append(randomRhyme)


for s in splitList:
    rhyme = rhymeSwap(s) 
     
#print(rhymesList)
rhymeStr = " ".join(rhymesList)

print(rhymeStr)



    
