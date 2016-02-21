import re
def regexStrip(string, chars='\s'):
    if chars != '\s':
        chars = '[' + chars + ']'
    regexFormat = '^' + chars + '*|' + chars + '*$' # Credit to Synes_Godt_Om on the reddit forum below. The pipe was the key.
    stripRegex = re.compile(regexFormat)            # https://www.reddit.com/r/inventwithpython/comments/3m3m3w/regex_version_of_strip_from_automate_the_boring/
    strippedString = stripRegex.sub('', string)
    print(strippedString)
    return strippedString

testString = '      Howdy World        '

regexStrip(testString)
