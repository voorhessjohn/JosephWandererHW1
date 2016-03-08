import shutil                                                                   # shutil module to rename files.
import os                                                                       # os module to get filenames and paths.
import re                                                                       # re module to check filenames.


def fillGaps(prefix):                                                           # The function takes a given prefix as an argument and fills the gaps in numbered sequences of .txt files with that prefix.
    filePattern = re.compile('(' + prefix + ')' + '(\\d\\d\\d)' + '(\.txt)$')   # compiles a regex to separate out the filenames of interest and to isolate the number part of those filename.
    fileList = list()                                                           # Initializes a variable to store a list of the files to check.
    for entry in os.listdir('.'):                                               # A for loop iterates over all the entries in the current directory.
        mo = filePattern.search(entry)                                          # It produces a match object by searching for the regex pattern in the entry.
        if mo == None:                                                          # If the match object is None then the entry was not one of the files to check.
            continue                                                                # So the for loop continues with the next entry in the directory.
        fileList.append(mo.group())                                             # But if a match was found it is a file to check so it is appended to the fileList as a string.
    sortedList = sorted(fileList)                                               # The fileList is sorted to compare the number in a filename with its place in the list. Leading zeros are needed for correct sorting.
    for i in range(len(sortedList)):                                            # A for loop is used to check each file in sortedList. range() is chosen to use the index of the list for comparison with the number in the filename.
        mo = filePattern.search(sortedList[i])                                  # The regex pattern is used again to work on the groups it finds.
        fileNum = mo.group(2)                                                   # Group 2 of the match object is the number in the filename that needs to be checked.
        fileExt = mo.group(3)                                                   # Group 3 is the .txt file extension.
        oldFilename = mo.group()                                                # The original filename is stored so the file can be identified for renaming later.
        rightNum = i + 1                                                        # The correct number in the sequence is the list index of the file +1 because list indices start at 0.
        if int(fileNum) != rightNum:                                            # An if statment compares the filename number with what it should be. If it isn't what it should be it will be renamed.
            if rightNum < 10:                                                   # To preserve the correct format with leading zeros they are added as strings when needed with if statements that check size.
                fileNum = '00' + str(rightNum)                                   
            elif rightNum < 100:
                fileNum = '0' + str(rightNum)
            else:
                fileNum = str(rightNum)                                         # The number in the filename is assigned the correct value
            newFilename = prefix + fileNum + fileExt                            # The new filename is produced by concatenating the given prefix, the correct formatted number and the file extension.
            absWorkingDir = os.path.abspath('.')                                # A correctly formatted string of the absolute path of the current directory is needed to produce paths of the files.
            oldFilename = os.path.join(absWorkingDir, oldFilename)              # oldFilename is assigned its full absolute path.
            newFilename = os.path.join(absWorkingDir, newFilename)              # The same is done for the new, correct filename.
            shutil.move(oldFilename, newFilename)                               # shutil.move() is used to rename the files. the old and new paths are used for its source and destination arguments respectively.

fillGaps('spam')
    
