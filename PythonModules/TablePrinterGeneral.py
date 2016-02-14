import copy
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(table):
    workTable = copy.deepcopy(table) # Making a dummy variable to derive attributes of the original list without altering the original list   
    colWidths = [0] * len(workTable) # Initializes a list with a number of values equal to the number of inner lists in the table. This makes a spot to store the highest length of strings in each inner list.
    for i in range(len(workTable)):
        for j in range(len(workTable[i])):
            workTable[i].sort(key=len,reverse=True) # Sorts the strings in each inner list by length(because key=len), with longest first(because reverse=True)
        colWidths[i] = len(workTable[i][0]) # Stores the length of the largest string of each list(which is at index 0 because of the sorting) in the colWidths list
    orderedTable = [] # Initializes a variable to store a list of lists of strings. Each list of strings is a row to be printed 
    for a in range(len(table[0])): # I'm using len(table[0]), ie. the length of the first list in the table, because I'm assuming the all the lists are of equal length
        orderedTable.append([]) # Appends an empty list for each row to be printed
        for b in range(len(table)):
            orderedTable[a].append(table[b][a]) # Fills each new empty list with the strings for each row in order
    for x in range(len(orderedTable)):
        for y in range(len(colWidths)):
            print(orderedTable[x][y].rjust(colWidths[y] + 1),end='') # Prints each row with amount of justification pulled from colWidths list, plus 1 for a space between columns. end="" prevents printing a new line in the middle of a row.
        print('') # Prints a new line after a row to separate rows. 

printTable(tableData)


