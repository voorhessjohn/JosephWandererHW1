import re, pprint, itertools

##########
#### This file contains three chunks of similar code that each derives a useful text file from the free and open pronunciation dictionary text file originally created by Carnegie Mellon University.
#### The CMU pronunciation dictionary is required for this code to run. It has been manually cleared of comments then renamed and referred to as sourceDict.txt in this code.
#### The CMU dictionary's flat file format looks like the text below
####
####ABACUS  AE1 B AH0 K AH0 S
####ABAD  AH0 B AA1 D
####
#### Each code chunk should probably be run separate from the others b/c they share some variables and file references.
##########


#### Note: To uncomment code in IDLE select the lines you want to uncomment, go to the 'Format' menu and select 'Uncomment Region' or use Alt+4


##########
####Dictionary Maker: The Keys: All the words in the CMU pronunciation dictionary (ie. sourceDict.txt). The Values: a string representing the pronunciation of each word using the CMU/Arpabet format.
##########
##cmuDictFile = open('.\sourceDict.txt')                        # Opens sourceDict.txt in read mode by default and stores it in cmuDictFile.
##cmuDictContents = list(cmuDictFile.readlines())               # Stores a list made of each line of cmuDictFile produced by calling the readlines() method on cmuDictFile.
##wordList = list()                                             # Makes a list that will store each word entry in sourceDict.txt.
##pronList = list()                                             # Does the same for each pronunciation entry.
##for i in range(len(cmuDictContents)):                         # Makes a for loop that will iterate on each line stored in the list in cmuDictContents.
##    split = re.split(r'\s\s', cmuDictContents[i])             # Uses the re module to split each line at the double space '  ' which separates the word from its pronunciation. Returns a list stored in split.
##    word = split[0]                                           # The word part is at index 0. Stored in the variable word.
##    wordList.append(word)                                     # Appends that word to wordList.
##    pron = split[1]                                           # The pronunciation part is at index 1. Stored in the variable pron.
##    pron = pron.rstrip()                                      # The trailing newline character on each line is removed with the rstrip() method.
##    pronList.append(pron)                                     # Appends that pronunciation to pronList.
##wordPronDict = dict(zip(wordList, pronList))                  # wordList and pronList should be in matching order. A Dict object is made from zipping them together.
##cmuDictFile.close()                                           # Closes cmuDictFile. Should probably be done earlier.
##
##wordPronDictFile = open('wordPronDictFile.txt', 'w')          # Opens a text file in write mode to store that Dict for later use.
##wordListFile = open('wordListFile.txt', 'w')                  # The lists were saved just for reference while writing code.
##pronListFile = open('pronListFile.txt', 'w')
##
##wordPronDictFile.write(str(wordPronDict))                     # Writes the Dict as a string in wordPronDictFile.
##wordListFile.write(str(wordList))
##pronListFile.write(str(pronList))
##
##pronListFile.close()
##wordListFile.close()
##wordPronDictFile.close()                                      # Closes the file.
##########





##########
####Dictionary Maker with Syllable Count: The Keys: All the words from sourceDict.txt. The Values: each value is a list with the pronunciation of a word at index 0 and a count of the syllables in that word at index 1.
#### The design is the same as above except where noted.
##########
##cmuDictFile = open('.\sourceDict.txt')
##cmuDictContents = list(cmuDictFile.readlines())
##wordList = list()
##pronList = list()                                             # pronList will be a list of lists. The entries in pronList will be lists of the pronunciation at index 0 and the syllable count at index 1.
##syllRegex = re.compile(r'\w*\d+')                             # This regex pattern catches vowels as encoded in CMU's format. The number of vowel sounds==syllables. Vowels are marked by a number as a stress indicator.
##for i in range(len(cmuDictContents)):
##    pronSyllList = list()
##    split = re.split(r'\s\s', cmuDictContents[i])
##    word = split[0]
##    wordList.append(word)
##    pron = split[1]
##    pron = pron.rstrip()
##    pronSyllCount = len(re.findall(syllRegex, pron))          # The syllable count is found by finding the length of the list returned by findall() using syllRegex on the pronunciation. 
##    pronSyllList.append(pron)                                 # pronSyllList will be a list that gets stored in the list in the pronList variable. the Pronunciation is appended first to occupy index 0
##    pronSyllList.append(pronSyllCount)                        # The syllable count occupies index 1
##    pronList.append(pronSyllList)                             # The pronSyllList is appended to pronList
##
##wordPronSyllDict = dict(zip(wordList, pronList))
##cmuDictFile.close()
##
##wordPronSyllDictFile = open('wordPronSyllDictFile.txt', 'w')
##wordListFile = open('wordListFile.txt', 'w')
##pronListFile = open('pronListFile.txt', 'w')
##
##wordPronSyllDictFile.write(str(wordPronSyllDict))
##wordListFile.write(str(wordList))
##pronListFile.write(str(pronList))
##
##pronListFile.close()
##wordListFile.close()
##wordPronDictFile.close()
##########



##########
####Hyphenated Word List Maker: Makes a list of the hyphenated words in the CMU dictionary that would otherwise be filtered out by the word list (enable1.txt) that is used by rhymeSwap() to remove proper nouns and other chaff from rhyme lists.
#### This code is the same as the first Dictionary Maker except where noted.
##########
##cmuDictFile = open('.\sourceDict.txt')
##cmuDictContents = list(cmuDictFile.readlines())
##wordList = list()
####pronList = list()                                       # The pronunciations are not needed
##hyphenList = list()
##for i in range(len(cmuDictContents)):
##    split = re.split(r'\s\s', cmuDictContents[i])
##    word = split[0]
##    wordList.append(word)
####    pron = split[1]                                     # Ditto
####    pron = pron.rstrip()                                # Ditto
####    pronList.append(pron)                               # Ditto
####wordPronDict = dict(zip(wordList, pronList))            # Don't need a new dictionary
##cmuDictFile.close()
##for i in range(len(wordList)):                            # A for loop iterates over each word in the original dictionary put in wordList.
##    if '-' in wordList[i]:                                # If the word has a hyphen in it:
##        hyphenList.append(wordList[i])                    # Appends the hyphenated word to hyphenList.
##hyphenString = '\n'.join(hyphenList)                      # Makes a string with a newline separating each hyphenated word.
##
##hyphenStringFile = open('hyphenStringFile.txt', 'w')      # Writes it to a file.
##hyphenStringFile.write(hyphenString)
##hyphenStringFile.close()
##########





########
###### This code was used to check that the word list and pronunciation list corresponded to each other correctly. It takes a word and prints its pronunciation if it was in the CMU dictionary.
########
####while True:
####    print('Find a word')
####    what = input()
####    what = what.upper()
####    if what == '':
####        break
####    elif what in wordList:
####        pos = wordList.index(what)
####        print(pronList[pos])
####    else:
####        print('Not found')
######



