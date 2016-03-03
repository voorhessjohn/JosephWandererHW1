import re, pprint

CMUDictFile = open('.\FlatDictPlain.txt')
CMUDictContents = list(CMUDictFile.readlines())
wordPronRegex = re.compile(r'(^.*\s\s)(.*\n)')
nativeDict = {}   
for i in range(len(CMUDictContents)):
    wordPronMo = wordPronRegex.search(CMUDictContents[i])
    word = wordPronMo.group(1)
    pron = wordPronMo.group(2)
    nativeDict[word] = pron
    pprint.pprint(nativeDict)


