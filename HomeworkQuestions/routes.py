from flask import *
from functools import wraps
import re, pprint, itertools, ast, random
app = Flask(__name__)

app.secret_key = 'something unique and secret'

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
    
    wordPronDictFile = open('wordPronDictFile.txt', 'r')
    wordPronDict = wordPronDictFile.read()
    wordPronDict = ast.literal_eval(wordPronDict)
    wordPronDictFile.close()

    pronWordDict4File = open('pronWordDict4File.txt', 'r')
    pronWordDict4 = pronWordDict4File.read()
    pronWordDict4 = ast.literal_eval(pronWordDict4)
    pronWordDict4File.close()

    pronWordDict3File = open('pronWordDict3File.txt', 'r')
    pronWordDict3 = pronWordDict3File.read()
    pronWordDict3 = ast.literal_eval(pronWordDict3)
    pronWordDict3File.close()

    pronWordDict2File = open('pronWordDict2File.txt', 'r')
    pronWordDict2 = pronWordDict2File.read()
    pronWordDict2 = ast.literal_eval(pronWordDict2)
    pronWordDict2File.close()

    pronWordDict1File = open('pronWordDict1File.txt', 'r')
    pronWordDict1 = pronWordDict1File.read()
    pronWordDict1 = ast.literal_eval(pronWordDict1)
    pronWordDict1File.close()

    pronWordDictStress4File = open('pronWordDictStress4File.txt', 'r')
    pronWordDictStress4 = pronWordDictStress4File.read()
    pronWordDictStress4 = ast.literal_eval(pronWordDictStress4)
    pronWordDictStress4File.close()

    pronWordDictStress3File = open('pronWordDictStress3File.txt', 'r')
    pronWordDictStress3 = pronWordDictStress3File.read()
    pronWordDictStress3 = ast.literal_eval(pronWordDictStress3)
    pronWordDictStress3File.close()

    pronWordDictStress2File = open('pronWordDictStress2File.txt', 'r')
    pronWordDictStress2 = pronWordDictStress2File.read()
    pronWordDictStress2 = ast.literal_eval(pronWordDictStress2)
    pronWordDictStress2File.close()

    pronWordDictStress1File = open('pronWordDictStress1File.txt', 'r')
    pronWordDictStress1 = pronWordDictStress1File.read()
    pronWordDictStress1 = ast.literal_eval(pronWordDictStress1)
    pronWordDictStress1File.close()

    if searchStringUp in wordPronDict.keys():
        #print('In Dict')
        searchPron = wordPronDict[searchStringUp]

        mo4String = ''
        mo3String = ''
        mo2String = ''
        mo1String = ''

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

        if tempRegex1.search(searchPron) != None:
            mo1String = str(tempRegex1.search(searchPron).group())
            mo1StringUnstressed = subRegex.sub('', mo1String)

        rhymeListBig = list()
        
        if mo4String in pronWordDictStress4.keys() and len(pronWordDictStress4.get(mo4String,[])) > 1:
            #print('stress4')
            rhymeList4 = pronWordDictStress4[mo4String]
            del rhymeList4[rhymeList4.index(searchStringUp)]
            for i in range(len(rhymeList4)):
                rhymeListBig.append(rhymeList4[i])

        if mo3String in pronWordDictStress3.keys() and len(pronWordDictStress3.get(mo3String,[])) > 1:
            #print('stress3')
            rhymeList3 = pronWordDictStress3[mo3String]
            del rhymeList3[rhymeList3.index(searchStringUp)]
            for i in range(len(rhymeList3)):
                rhymeListBig.append(rhymeList3[i])

        if mo2String in pronWordDictStress2.keys() and len(pronWordDictStress2.get(mo2String,[])) > 1:
            #print('stress2')
            rhymeList2 = pronWordDictStress2[mo2String]
            del rhymeList2[rhymeList2.index(searchStringUp)]
            for i in range(len(rhymeList2)):
                rhymeListBig.append(rhymeList2[i])
#            randomRhyme = prettyRegex.sub('', randomRhyme)
#            randomRhyme = random.choice(rhymeList2)
#            print(randomRhyme)

        elif mo1String in pronWordDictStress1.keys() and len(pronWordDictStress1.get(mo1String,[])) > 1:
            #print('stress1')
            rhymeList1 = pronWordDictStress1[mo1String]
            del rhymeList1[rhymeList1.index(searchStringUp)]
            for i in range(len(rhymeList1)):
                rhymeListBig.append(rhymeList1[i])

        if len(rhymeListBig) < 1:
            if mo4StringUnstressed in pronWordDict4.keys() and len(pronWordDict4.get(mo4StringUnstressed,[])) > 1:
                #print('4')
                rhymeList4 = pronWordDict4[mo4StringUnstressed]
                del rhymeList4[rhymeList4.index(searchStringUp)]
                for i in range(len(rhymeList4)):
                    rhymeListBig.append(rhymeList4[i])

            if mo3StringUnstressed in pronWordDict3.keys() and len(pronWordDict3.get(mo3StringUnstressed,[])) > 1:
                #print('3')
                rhymeList3 = pronWordDict3[mo3StringUnstressed]
                del rhymeList3[rhymeList3.index(searchStringUp)]
                for i in range(len(rhymeList3)):
                    rhymeListBig.append(rhymeList3[i])

            if mo2StringUnstressed in pronWordDict2.keys() and len(pronWordDict2.get(mo2StringUnstressed,[])) > 1:
                #print('2')
                rhymeList2 = pronWordDict2[mo2StringUnstressed]
                del rhymeList2[rhymeList2.index(searchStringUp)]
                for i in range(len(rhymeList2)):
                    rhymeListBig.append(rhymeList2[i])

            elif mo1StringUnstressed in pronWordDict1.keys() and len(pronWordDict1.get(mo1StringUnstressed,[])) > 1:
                #print('1')
                rhymeList1 = pronWordDict1[mo1StringUnstressed]
                del rhymeList1[rhymeList1.index(searchStringUp)]
                for i in range(len(rhymeList1)):
                    rhymeListBig.append(rhymeList1[i])


        if len(rhymeListBig) > 0:
            #print(rhymeListBig)
            randomRhyme = random.choice(rhymeListBig)
            randomRhyme = prettyRegex.sub('', randomRhyme)
            randomRhyme = randomRhyme.lower()
            return randomRhyme
        else:
            return searchString

@app.route('/')
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

@app.route('/input', methods=['GET', 'POST'])
def input():
    error = None
    if request.method == 'POST':
        splitList = request.form['lyrics'].split(' ')
        rhymesList = []
        for s in splitList:
            rhymesList.append(rhymeSwap(s))
        rhymeStr = " ".join(rhymesList)
        return rhymeStr

    return render_template('input.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
