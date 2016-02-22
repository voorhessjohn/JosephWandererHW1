import re
def regexStrip(string, chars='\s'):                 # 2 positional arguments. string must be present. chars has '\s' as the default, ie. the whitespace character class.
    if chars != '\s':                               # Checks to see if the user picked some other set of characters to strip. Must be a string.
        chars = '[' + chars + ']'                   # Puts the characters chosen by the user into brackets to make it a custom character class.
    regexFormat = '^' + chars + '*|' + chars + '*$' # Inserts the characters to be stripped into the appropriate regex format. '^' to catch leading characters. '$' to catch trailing characters. '*' for both to catch any number of the relevant characters. '|' to separate the leading and trailing parts of the regex and make sure both are checked, I think.
    stripRegex = re.compile(regexFormat)            # Turns the string into a regex object. Credit to Synes_Godt_Om on the following reddit forum for a close match of the regex needed. The pipe was the key. https://www.reddit.com/r/inventwithpython/comments/3m3m3w/regex_version_of_strip_from_automate_the_boring/
    strippedString = stripRegex.sub('', string)     # The 'sub'/substitution method is used to replace the caught characters with empty strings, effectively deleting them.
    print(strippedString)
    return strippedString

testString = '      Howdy World        '

regexStrip(testString)
