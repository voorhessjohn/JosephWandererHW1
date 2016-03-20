import re, pprint, ast

########
## These chunks of similar code use the Word:Pronunciation dictionary that is made by wordPronDictMaker.py to make dictionaries of rhyming sets of words.
## For these rhyme dictionaries the Key is the pronunciation at the end of a word and the Value is a list of all the words that end with that pronunciation, ie. rhyme sets.
## Different .txt files are created to accomodate different degrees of rhyme fit and word length.
## How well the rhymes fit is determined by the regex used to group them, namely the number of ending phonemes it captures and how it considers stressed syllables.
## Stress is encoded by a number that follows the vowel part of a syllable. 0 represents no stress, 1 for primary stress, 2 for secondary stress.
## Perfect rhymes are words whose pronunciations are the same from the primary stress to the end of the word.
########

#### Note: To uncomment code in IDLE select the lines you want to uncomment, go to the 'Format' menu and select 'Uncomment Region' or use Alt+4

########
## Stress-Blind Rhyming Dictionary Maker: Makes 4 dictionaries that match ending phonemes regardless of stress or vowel placement ie. near rhymes.
########
##pronWordDict4 = dict()                                        # Makes Dict objects and stores them in unique variables
##pronWordDict3 = dict()
##pronWordDict2 = dict()
##pronWordDict1 = dict()
##
##wordPronDictFile = open('wordPronDictFile.txt', 'r')          # Opens the Word:Pronunciation dictionary made by wordPronDictMaker.py in read-only mode.
##wordPronDict = wordPronDictFile.read()                        # Reads and stores the contents of the wordPronDictFile File object as a string.
##wordPronDict = ast.literal_eval(wordPronDict)                 # The ast module is used to convert the string from wordPronDictFile into a Dict object.
##wordPronDictFile.close()                                      # Closes the file
##
##subRegex = re.compile(r'\d')                                  # The regex r'\d' will be used in the sub() substitution method to remove the numbers that indicate stress.
##
##stripPattern4 = r'\w*\d? \w*\d? \w*\d? \w*\d?$'               # The regex to catch any phoneme is '\w*\d?'.
##stripPattern3 = r'\w*\d? \w*\d? \w*\d?$'                      # '\w*' catches the letter part of the phoneme.
##stripPattern2 = r'\w*\d? \w*\d?$'                             # The '\d?' part is used to ignore numbers, ie. whether or not the phoneme is a vowel. Vowels have numbers as stress indicators.
##stripPattern1 = r'\w*\d?$'                                    # Each phoneme is separated by a space like in the original CMU dictionary.
##
##tempRegex4 = re.compile(stripPattern4)                        # Compiles each regex for use in the search() method.
##tempRegex3 = re.compile(stripPattern3)
##tempRegex2 = re.compile(stripPattern2)
##tempRegex1 = re.compile(stripPattern1)
##
##
##for k, v in wordPronDict.items():                             # Makes a for loop that iterates over the Key(k) and Value(v) pairs(items) in the Word:Pronunciation dictionary(wordPronDict).
##    moTest4 = tempRegex4.search(v)                            # Makes and stores a Match object from a search() method called on the regex with the designated number of phonemes(4 here). It's passed the dict entry's value(v) ie. the pronunciation of a word.
##    if moTest4 != None:                                       # If there is a match made: ie. The Match object is not None: (A match will be made when the pronunciation has at least as many phonemes as designated(4).)
##        rhymeSet4 = subRegex.sub('',str(moTest4.group()))     # Removes the stress markers(numbers) from the pronunciation(Match).(calls sub() method on subRegex(r'/d' for numbers), passing it the '' empty string as replacement and, for string, a string made from the group() method called on the match object(the pronunciation).).
##        pronWordDict4.setdefault(rhymeSet4,[]).append(k)      # Makes pronWordDict4 a Pronunciation:Wordlist dictionary. Appends the word(k) to a list that is assured to be a Value with the pronunciation as its Key in the pronWordDict4 Dict by using the setdefault() method.
##
##for k, v in wordPronDict.items():                             # Same as above but with a 3 phoneme regex for the 3 phoneme dictionary.
##    moTest3 = tempRegex3.search(v)
##    if moTest3 != None:
##        rhymeSet3 = subRegex.sub('',str(moTest3.group()))
##        pronWordDict3.setdefault(rhymeSet3,[]).append(k)
##
##for k, v in wordPronDict.items():
##    moTest2 = tempRegex2.search(v)
##    if moTest2 != None:
##        rhymeSet2 = subRegex.sub('',str(moTest2.group()))
##        pronWordDict2.setdefault(rhymeSet2,[]).append(k)
##
##for k, v in wordPronDict.items():
##    moTest1 = tempRegex1.search(v)
##    if moTest1 != None:
##        rhymeSet1 = subRegex.sub('',str(moTest1.group()))
##        pronWordDict1.setdefault(rhymeSet1,[]).append(k)
##
##                                                          #Note: I made separate dictionaries for different numbers of matching phonemes to more easily refine word inclusion in rhymeSwap().
##                                                          #      I wanted to avoid bad rhymes that will be common when its only 1 or 2 matching phonemes.
##
##pronWordDict4File = open('pronWordDict4File.txt', 'w')        # Makes or overwrites a text file named pronWordDict4File.txt and stores the File object in write mode to pronWordDict4File.
##pronWordDict4File.write(str(pronWordDict4))                   # Makes a string out of the pronWordDict4 Dict made in the for loop above and writes it to the pronWordDict4File File.
##pronWordDict4File.close()                                     # Closes pronWordDict4File. The dictionary is now available as a text file for use in the rhymeSwap() function.
##
##pronWordDict3File = open('pronWordDict3File.txt', 'w')
##pronWordDict3File.write(str(pronWordDict3))
##pronWordDict3File.close()
##
##pronWordDict2File = open('pronWordDict2File.txt', 'w')
##pronWordDict2File.write(str(pronWordDict2))
##pronWordDict2File.close()
##
##pronWordDict1File = open('pronWordDict1File.txt', 'w')
##pronWordDict1File.write(str(pronWordDict1))
##pronWordDict1File.close()
########




########
## Stress-Sensitive Rhyming Dictionary Maker: Makes 8 dictionaries of sets of near perfect rhymes.
##  The design is basically the same as above except where noted.
########
##pronWordDictStress8 = dict()
##pronWordDictStress7 = dict()
##pronWordDictStress6 = dict()
##pronWordDictStress5 = dict()
##pronWordDictStress4 = dict()
##pronWordDictStress3 = dict()
##pronWordDictStress2 = dict()
##pronWordDictStress1 = dict()
##
##wordPronDictFile = open('wordPronDictFile.txt', 'r')
##wordPronDict = wordPronDictFile.read()
##wordPronDict = ast.literal_eval(wordPronDict)
##wordPronDictFile.close()
##
##
##stripPatternStress8 = r'\w*[12] \w*0? \w*0? \w*0? \w*0? \w*0? \w*0? \w*\0?$'      # The leading phonemes are stressed vowels (\w*[12]) and all phonemes match exactly including stress.
##stripPatternStress7 = r'\w*[12] \w*0? \w*0? \w*0? \w*0? \w*0? \w*\0?$'            # '\w*0?' was designed to include unstressed vowels and consonants but not stressed vowels. Doesn't quite work that way though.
##stripPatternStress6 = r'\w*[12] \w*0? \w*0? \w*0? \w*0? \w*\0?$'                  # 8 Dictionaries are made in order to include longer words in which the stress is near the beginning of the word.
##stripPatternStress5 = r'\w*[12] \w*0? \w*0? \w*0? \w*\0?$'
##stripPatternStress4 = r'\w*[12] \w*0? \w*0? \w*0?$'
##stripPatternStress3 = r'\w*[12] \w*0? \w*0?$'
##stripPatternStress2 = r'\w*[12] \w*0?$'
##stripPatternStress1 = r'\w*[12]$'
##
##                                                                              #Note: The '\w*0?' part of the regex does not behave as I expected.
##                                                                              #      It includes stressed syllables (ie. vowels encoded with 1 or 2)
##                                                                              #      which I thought would be excluded by the '0?' part.
##
##tempRegexStress8 = re.compile(stripPatternStress8)
##tempRegexStress7 = re.compile(stripPatternStress7)
##tempRegexStress6 = re.compile(stripPatternStress6)
##tempRegexStress5 = re.compile(stripPatternStress5)
##tempRegexStress4 = re.compile(stripPatternStress4)
##tempRegexStress3 = re.compile(stripPatternStress3)
##tempRegexStress2 = re.compile(stripPatternStress2)
##tempRegexStress1 = re.compile(stripPatternStress1)
##
##
##for k, v in wordPronDict.items():                                                 # Same as the for loops above except
##    moTestStress8 = tempRegexStress8.search(v)
##    if moTestStress8 != None:
##        rhymeSetStress8 = str(moTestStress8.group())
##        pronWordDictStress8.setdefault(rhymeSetStress8,[]).append(k)              # the sub() method is not called here. 
##
##for k, v in wordPronDict.items():
##    moTestStress7 = tempRegexStress7.search(v)
##    if moTestStress7 != None:
##        rhymeSetStress7 = str(moTestStress7.group())
##        pronWordDictStress7.setdefault(rhymeSetStress7,[]).append(k)
##
##for k, v in wordPronDict.items():
##    moTestStress6 = tempRegexStress6.search(v)
##    if moTestStress6 != None:
##        rhymeSetStress6 = str(moTestStress6.group())
##        pronWordDictStress6.setdefault(rhymeSetStress6,[]).append(k)
##
##for k, v in wordPronDict.items():
##    moTestStress5 = tempRegexStress5.search(v)
##    if moTestStress5 != None:
##        rhymeSetStress5 = str(moTestStress5.group())
##        pronWordDictStress5.setdefault(rhymeSetStress5,[]).append(k)
##
##
##for k, v in wordPronDict.items():
##    moTestStress4 = tempRegexStress4.search(v)
##    if moTestStress4 != None:
##        rhymeSetStress4 = str(moTestStress4.group())
##        pronWordDictStress4.setdefault(rhymeSetStress4,[]).append(k)
##
##for k, v in wordPronDict.items():
##    moTestStress3 = tempRegexStress3.search(v)
##    if moTestStress3 != None:
##        rhymeSetStress3 = str(moTestStress3.group())
##        pronWordDictStress3.setdefault(rhymeSetStress3,[]).append(k)
##
##for k, v in wordPronDict.items():
##    moTestStress2 = tempRegexStress2.search(v)
##    if moTestStress2 != None:
##        rhymeSetStress2 = str(moTestStress2.group())
##        pronWordDictStress2.setdefault(rhymeSetStress2,[]).append(k)
##
##for k, v in wordPronDict.items():
##    moTestStress1 = tempRegexStress1.search(v)
##    if moTestStress1 != None:
##        rhymeSetStress1 = str(moTestStress1.group())
##        pronWordDictStress1.setdefault(rhymeSetStress1,[]).append(k)
##
##
##pronWordDictStress8File = open('pronWordDictStress8File.txt', 'w')
##pronWordDictStress8File.write(str(pronWordDictStress8))
##pronWordDictStress8File.close()
##
##pronWordDictStress7File = open('pronWordDictStress7File.txt', 'w')
##pronWordDictStress7File.write(str(pronWordDictStress7))
##pronWordDictStress7File.close()
##
##pronWordDictStress6File = open('pronWordDictStress6File.txt', 'w')
##pronWordDictStress6File.write(str(pronWordDictStress6))
##pronWordDictStress6File.close()
##
##pronWordDictStress5File = open('pronWordDictStress5File.txt', 'w')
##pronWordDictStress5File.write(str(pronWordDictStress5))
##pronWordDictStress5File.close()
##
##pronWordDictStress4File = open('pronWordDictStress4File.txt', 'w')
##pronWordDictStress4File.write(str(pronWordDictStress4))
##pronWordDictStress4File.close()
##
##pronWordDictStress3File = open('pronWordDictStress3File.txt', 'w')
##pronWordDictStress3File.write(str(pronWordDictStress3))
##pronWordDictStress3File.close()
##
##pronWordDictStress2File = open('pronWordDictStress2File.txt', 'w')
##pronWordDictStress2File.write(str(pronWordDictStress2))
##pronWordDictStress2File.close()
##
##pronWordDictStress1File = open('pronWordDictStress1File.txt', 'w')
##pronWordDictStress1File.write(str(pronWordDictStress1))
##pronWordDictStress1File.close()
########






            
