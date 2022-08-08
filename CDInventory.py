#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KSwanson, 2022-Aug-07, Edited File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
# Complete
lstRow = {"id":"string", "Title":"string","Artist":"string"} # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        # Complete
        print("Enter File Name: ")
        FileNameResponse = input()
        inputFile = open(FileNameResponse, "r")
        for line in inputFile:
            parsedLine = line.split(",")
            lstRow["id"] = parsedLine[0]
            lstRow["Title"] = parsedLine[1]
            lstRow["Artist"] = parsedLine[2]
            lstTbl.append(lstRow.copy())
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow["id"] = strID
        lstRow["Title"] = strTitle
        lstRow["Artist"] = strArtist
        lstTbl.append(lstRow.copy())
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row.values())
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        # Complete
        print("Provide ID to be deleted: ")
        deleteID=input()
        for row in lstTbl:
            if row["id"] == deleteID:
                lstTbl.remove(row)
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

