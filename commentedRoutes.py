from flask import *
from functools import wraps
import re, pprint, ast, random
app = Flask(__name__)

app.secret_key = 'something unique and secret'


subRegex = re.compile(r'\d')                               # The regex r'\d' will be used in the sub() substitution method to remove the numbers that indicate stress.

prettyRegex = re.compile(r'\(\d\)')

stripPattern4 = r'\w*\d? \w*\d? \w*\d? \w*\d?$'             # The regex to catch any phoneme is '\w*\d?'.
stripPattern3 = r'\w*\d? \w*\d? \w*\d?$'                    # '\w*' catches the letter part of the phoneme.
stripPattern2 = r'\w*\d? \w*\d?$'                           # The '\d?' part is used to ignore numbers, ie. whether or not the phoneme is a vowel. Vowels have numbers as stress indicators.
stripPattern1 = r'\w*\d?$'                                  # Each phoneme is separated by a space like in the original CMU dictionary.

tempRegex4 = re.compile(stripPattern4)                      # Compiles each regex for use in the search() method.
tempRegex3 = re.compile(stripPattern3)
tempRegex2 = re.compile(stripPattern2)
tempRegex1 = re.compile(stripPattern1)

wordPronDictFile = open('/home/joewand/mysite/wordPronDictFile.txt', 'r')           #opens wordPronDictFile Word:Pronunciation dictionary in read only mode.
wordPronDict = wordPronDictFile.read()                                              #stores Word:Pronunciation dictionary as variable wordPronDict
wordPronDict = ast.literal_eval(wordPronDict)                                       #runs ast.literal_eval on wordPronDict to allow string to run as code
wordPronDictFile.close()                                                            #closes the file on the server with the variable extant and initialized

wordPronSyllDictFile = open('/home/joewand/mysite/wordPronSyllDictFile.txt', 'r')   #opens dict file with syllable value for word key
wordPronSyllDict = wordPronSyllDictFile.read()
wordPronSyllDict = ast.literal_eval(wordPronSyllDict)
wordPronSyllDictFile.close()

pronWordDict4File = open('/home/joewand/mysite/pronWordDict4File.txt', 'r')         #opens 4 phoneme dictionary
pronWordDict4 = pronWordDict4File.read()
pronWordDict4 = ast.literal_eval(pronWordDict4)
pronWordDict4File.close()

pronWordDict3File = open('/home/joewand/mysite/pronWordDict3File.txt', 'r')         #opens 3 phoneme dictionary
pronWordDict3 = pronWordDict3File.read()
pronWordDict3 = ast.literal_eval(pronWordDict3)
pronWordDict3File.close()

pronWordDict2File = open('/home/joewand/mysite/pronWordDict2File.txt', 'r')         #opens 2 phoneme dictionary
pronWordDict2 = pronWordDict2File.read()
pronWordDict2 = ast.literal_eval(pronWordDict2)
pronWordDict2File.close()

pronWordDict1File = open('/home/joewand/mysite/pronWordDict1File.txt', 'r')         #opens single phoneme dictionary
pronWordDict1 = pronWordDict1File.read()
pronWordDict1 = ast.literal_eval(pronWordDict1)
pronWordDict1File.close()

pronWordDictStress4File = open('/home/joewand/mysite/pronWordDictStress4File.txt', 'r') #opens dictionary of complete matching rhyme sets featuring 4 matching phonemes
pronWordDictStress4 = pronWordDictStress4File.read()
pronWordDictStress4 = ast.literal_eval(pronWordDictStress4)
pronWordDictStress4File.close()

pronWordDictStress3File = open('/home/joewand/mysite/pronWordDictStress3File.txt', 'r') #opens dictionary of complete matching rhyme sets featuring 3 matching phonemes
pronWordDictStress3 = pronWordDictStress3File.read()
pronWordDictStress3 = ast.literal_eval(pronWordDictStress3)
pronWordDictStress3File.close()

pronWordDictStress2File = open('/home/joewand/mysite/pronWordDictStress2File.txt', 'r') #opens dictionary of complete matching rhyme sets featuring 2 matching phonemes
pronWordDictStress2 = pronWordDictStress2File.read()
pronWordDictStress2 = ast.literal_eval(pronWordDictStress2)
pronWordDictStress2File.close()

pronWordDictStress1File = open('/home/joewand/mysite/pronWordDictStress1File.txt', 'r') #opens dictionary of complete matching rhyme sets featuring 1 matching phoneme
pronWordDictStress1 = pronWordDictStress1File.read()
pronWordDictStress1 = ast.literal_eval(pronWordDictStress1)
pronWordDictStress1File.close()

hyphenListFile = open('/home/joewand/mysite/hyphenStringFileEditList.txt', 'r') #opens dictionary of hyphenated words 
hyphenList = hyphenListFile.read()
hyphenList = ast.literal_eval(hyphenList)
hyphenListFile.close()

enable1File = open('/home/joewand/mysite/enable1.txt', 'r') #opens list of words that are NOT proper nouns
enable1List = enable1File.readlines()
enable1File.close()
for i in range(len(enable1List)):
    enable1List[i] = enable1List[i].rstrip()    #rstrip() method removes whitespace
    enable1List[i] = enable1List[i].upper()     #upper() method makes all letters uppercase


def rhymeSwap(searchString):

    searchStringUp = searchString.upper()   #makes user input all uppercase




    if searchStringUp in wordPronDict.keys():   #checks to see if user input is in main dictionary
        #print('In Dict')
        searchPron = wordPronDict[searchStringUp]   #initializes variable for pronunciation values at key location of user input
        searchStringSyllCount = wordPronSyllDict[searchStringUp][1] #initializes variable for number of syllables in user input

        mo4String = ''                                  #initializing variables used below
        mo3String = ''
        mo2String = ''
        mo1String = ''

        mo4StringUnstressed = ''
        mo3StringUnstressed = ''
        mo2StringUnstressed = ''
        mo1StringUnstressed = ''


        if tempRegex4.search(searchPron) != None:                       #if searchPron (variable containing pronunciation values of user input) returns a match from tempRegex4
            mo4String = str(tempRegex4.search(searchPron).group())      #mo4String variable is pronunciation value of user input
            mo4StringUnstressed = subRegex.sub('', mo4String)           #mo4StringUnstressed is mo4String pronunciation variable without numbers that indicate stress

        if tempRegex3.search(searchPron) != None:
            mo3String = str(tempRegex3.search(searchPron).group())
            mo3StringUnstressed = subRegex.sub('', mo3String)

        if tempRegex2.search(searchPron) != None:
            mo2String = str(tempRegex2.search(searchPron).group())
            mo2StringUnstressed = subRegex.sub('', mo2String)

        if tempRegex1.search(searchPron) != None:
            mo1String = str(tempRegex1.search(searchPron).group())
            mo1StringUnstressed = subRegex.sub('', mo1String)

        rhymeListBig = list()

        if mo4String in pronWordDictStress4.keys() and len(pronWordDictStress4.get(mo4String,[])) > 1: #if mo4String matches a value in the 4-syllable stress dict and the stress value is greater than 1 
            #print('stress4')
            rhymeList4 = pronWordDictStress4[mo4String]         #stores values of pronWordDictStress4 aat ke mo4String in variable rhymeList4
            if searchStringUp in rhymeList4:                    #checks to see if user input is in the list stored in the new rhymeList4 variable
                del rhymeList4[rhymeList4.index(searchStringUp)] #if so, deletes user input from that list (so as to not return the users original word as a rhyme)
            for i in range(len(rhymeList4)):                    #appends all items in rhymeList4 to rhymeListBig
                rhymeListBig.append(rhymeList4[i])

        if mo3String in pronWordDictStress3.keys() and len(pronWordDictStress3.get(mo3String,[])) > 1:
            #print('stress3')
            rhymeList3 = pronWordDictStress3[mo3String]
            if searchStringUp in rhymeList3:
                del rhymeList3[rhymeList3.index(searchStringUp)]
            for i in range(len(rhymeList3)):
                rhymeListBig.append(rhymeList3[i])

        if mo2String in pronWordDictStress2.keys() and len(pronWordDictStress2.get(mo2String,[])) > 1:
            #print('stress2')
            rhymeList2 = pronWordDictStress2[mo2String]
            if searchStringUp in rhymeList2:
                del rhymeList2[rhymeList2.index(searchStringUp)]
            for i in range(len(rhymeList2)):
                rhymeListBig.append(rhymeList2[i])
#            randomRhyme = prettyRegex.sub('', randomRhyme)
#            randomRhyme = random.choice(rhymeList2)
#            print(randomRhyme)

        if mo1String in pronWordDictStress1.keys() and len(pronWordDictStress1.get(mo1String,[])) > 1:
            #print('stress1')
            rhymeList1 = pronWordDictStress1[mo1String]
            if searchStringUp in rhymeList1:
                del rhymeList1[rhymeList1.index(searchStringUp)]
            for i in range(len(rhymeList1)):
                rhymeListBig.append(rhymeList1[i])

        if len(rhymeListBig) < 1:                                           #if nothing is in rhymeListBig yet
            if mo4StringUnstressed in pronWordDict4.keys() and len(pronWordDict4.get(mo4StringUnstressed,[])) > 1:
                #print('4')
                rhymeList4 = pronWordDict4[mo4StringUnstressed]             #creates variable  for unstressed keys
                if searchStringUp in rhymeList4:                            #works the same as mo4String above
                    del rhymeList4[rhymeList4.index(searchStringUp)]
                for i in range(len(rhymeList4)):
                    rhymeListBig.append(rhymeList4[i])

            if mo3StringUnstressed in pronWordDict3.keys() and len(pronWordDict3.get(mo3StringUnstressed,[])) > 1:
                #print('3')
                rhymeList3 = pronWordDict3[mo3StringUnstressed]
                if searchStringUp in rhymeList3:
                    del rhymeList3[rhymeList3.index(searchStringUp)]
                for i in range(len(rhymeList3)):
                    rhymeListBig.append(rhymeList3[i])

            elif mo2StringUnstressed in pronWordDict2.keys() and len(pronWordDict2.get(mo2StringUnstressed,[])) > 1:
                #print('2')
                rhymeList2 = pronWordDict2[mo2StringUnstressed]
                if searchStringUp in rhymeList2:
                    del rhymeList2[rhymeList2.index(searchStringUp)]
                for i in range(len(rhymeList2)):
                    rhymeListBig.append(rhymeList2[i])

            elif mo1StringUnstressed in pronWordDict1.keys() and len(pronWordDict1.get(mo1StringUnstressed,[])) > 1:
                #print('1')
                rhymeList1 = pronWordDict1[mo1StringUnstressed]
                if searchStringUp in rhymeList1:
                    del rhymeList1[rhymeList1.index(searchStringUp)]
                for i in range(len(rhymeList1)):
                    rhymeListBig.append(rhymeList1[i])

        removeList = list()                             
        if len(rhymeListBig) > 0:
            for i in range(len(rhymeListBig)):
                #rhymeListBig[i] = prettyRegex.sub('', rhymeListBig[i])     #oldWorking
                if rhymeListBig[i] not in hyphenList and rhymeListBig[i] not in enable1List:    #filters hyphenated words and proper names out of rhymeListBig
                    removeList.append(rhymeListBig[i])
            if searchStringUp in rhymeListBig:       #another chance to remove the original input from the rhymeListBig
                removeList.append(searchStringUp)    #test
        for word in removeList:
            rhymeListBig.remove(word)
        for i in range(len(rhymeListBig)):                          #test
            rhymeListBig[i] = prettyRegex.sub('', rhymeListBig[i])  #test


        if len(rhymeListBig) > 0:
            #print(rhymeListBig)
            syllMatchList = list()
            for word in rhymeListBig:
                wordSyllCount = wordPronSyllDict[word][1]           #filters rhymeListBig to match the number of syllables in the original user input
                if wordSyllCount == searchStringSyllCount:
                    syllMatchList.append(word)
            if len(syllMatchList) > 0:
                randomRhyme = random.choice(syllMatchList)          #returns syllable match if there is one
                randomRhyme = prettyRegex.sub('', randomRhyme)
                randomRhyme = randomRhyme.lower()
                return randomRhyme
            elif len(syllMatchList) == 0:
                randomRhyme = random.choice(rhymeListBig)
                randomRhyme = prettyRegex.sub('', randomRhyme)      #returns regular match if there isn't a syllable match
                randomRhyme = randomRhyme.lower()
                return randomRhyme
        else:
            return searchString                                     #If there's no match at all, it returns the user input instead of a rhyme

@app.route('/input')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
	    if 'logged_in' in session:
                return test(*args, **kwargs)
	    else:
                flash('You need to login first.')
                return redirect(url_for('log'))
    return wrap

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect (url_for('log'))

@app.route('/hello')
@login_required
def hello():
    return render_template('hello.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('hello'))
    return render_template('log.html', error=error)

@app.route('/', methods=['GET', 'POST'])
def input():                                                            #establishes a user input field to accept lyrics
    error = None
    if request.method == 'POST':
        rawLyrics = request.form['lyrics']                              #stores user lyrics in a variable called rawLyrics
        if rawLyrics == '':                                             #checks to make sure that there's some lyrics
            error = 'Please input some lyrics.'
        else:
            rawWordsToSwap = request.form['swap']
            if rawWordsToSwap != []:
                wordsToSwapList = rawWordsToSwap.split()                #takes user input and splits it into a list of words
                wordsToSwapList = list(filter(None,wordsToSwapList))
            else:
                wordsToSwapList = []

        #wordsToSwapList = request.form['swap'].split(' ')
            rhymesList = []
            if wordsToSwapList == []:
                wordsToSwapList = re.split('\W+',rawLyrics)             #if no words to swap are specified, all lyrics are split into a list to be swapped
                wordsToSwapList = list(filter(None,wordsToSwapList))
                shortList = []
                for word in wordsToSwapList:
                    if word not in shortList:
                        shortList.append(word)
                wordsToSwapList = shortList
                wordsToSwapList = list(filter(None,wordsToSwapList))

            for i in range(len(wordsToSwapList)):
                rhymesList.append(rhymeSwap(wordsToSwapList[i]))
            swapDict = dict(zip(wordsToSwapList, rhymesList))
            for word in wordsToSwapList:
                swapRegex = re.compile('\\b(' + str(word) + ')\\b', flags=re.IGNORECASE)
                try:
                    rawLyrics = re.sub(swapRegex, swapDict[word],rawLyrics)
                except (TypeError, KeyError, ValueError):
                    continue
            br = '<br>'
            rawLyrics = re.sub(r'\r\n', br, rawLyrics)
            #rawLyrics.replace('\r\n',r).replace('\n\r',r).replace('\r',r).replace('\n',r)
            #return rawLyrics
            return '<big>' + rawLyrics + '</big>'


    return render_template('input.html', error=error)

if __name__ == '__main__':
    app.run()

