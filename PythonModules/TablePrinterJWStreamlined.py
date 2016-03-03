import copy                          # copy for sorting lists safely
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(table):
    workTable = copy.deepcopy(table) # Makes a variable to store a copy of the list to sort the list without altering the original list   
    colWidths = [0] * len(workTable) # Initializes a list with a number of values equal to the number of lists in the table. This makes a spot to store the length of the longest string in each list.
    for i in range(len(workTable)):  # For each list in the table
        workTable[i].sort(key=len)   # Sorts the strings in that list by length(because key=len)
        colWidths[i] = len(workTable[i][-1]) # Stores the length of the largest string of each list(which is at the end of the list because of the sorting) in the colWidths list
    for a in range(len(table[0])):   # For each row to be printed ie. the length of the lists in the table, which are assumed to be equal
        for b in range(len(table)):  # For each column to be printed ie. the number of lists in the table
            print(table[b][a].rjust(colWidths[b] + 1),end='') # Prints each row with each column having it's justification pulled from colWidths list, + 1 for a space between columns. end="" prevents printing a new line in the middle of a row.
        print('')                    # Prints a new line after a row to separate rows. 

printTable(tableData)


