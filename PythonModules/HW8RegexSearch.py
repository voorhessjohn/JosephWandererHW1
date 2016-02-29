import re, os                                           # re module for regex, os for listdir() and join()

def regexSearchFiles(userRegex, path='.'):              # 2 postitional arguments. The 1st is the user supplied regex expression, which is required. The second is the path for the folder to be searched, which is assigned the cwd by default.
    regex = re.compile(userRegex)                       # Makes the user-supplied regex into a regex object.
    fileList = os.listdir(path)                         # Produces a list of the filenames in the specified folder or in the cwd if no folder is specified.
    for filename in fileList:                           # Iterates over the filenames in the list produced by os.listdir().
        if filename.endswith('.txt'):                   # Specifies .txt files as the filetype to search.
            file = open(os.path.join(path, filename))   # Opens a .txt file in read mode and stores the resultant file object in a variable named file.
            fileString = file.read()                    # Produces a single string of the file contents and stores it in a variable named fileString.
            mo = regex.findall(fileString)              # Uses the findall method taking the user's regex and executing over fileString to produce a list of matches. The list of matches is stored to the variable mo.
            if mo != []:                                # Ignores files with no matches ie. when findall() results in an empty list.
                print(filename)                         # Prints the filename of the file in which matches were found.
                print(mo)                               # Prints the list of matches
            file.close()                                # Closes the file

regexBase = input('Please Enter a regex: ')             # Takes user input for the regex
regexSearchFiles(regexBase)                             # The function call
