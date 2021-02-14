#------------------------------------------#
# Title: CDInventory.py
# Desc: Updated Starter Script for Assignment completing "TODOs" and adding dictionary lists
# Change Log: (Who, When, What)
# Mpost, 1100-FEB-12, Created File
#------------------------------------------#

#Modified Variables from starter script to include dictionary structure

strChoice = '' # User input
dicRow1 = {'id':'This is CD ID', 'Title': 'Title Of Song ','Artist': 'Artist of Song'} # I was having issues with the delete function not deleting 
#the first row adding this sample placeholder row seemed to fix that
dicRow = {} # Empty Dictionary 
lstTbl = [] #Empty list
lstTbl.append(dicRow1) #list appending dictionary to create 2d list 
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


print('The Magic CD Inventory\n')
while True:
 
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory') # this information unchanged from Starter
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    
    if strChoice == 'x': # No need to change from Starter
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l': # Load function I included the strip utility from the example in lab 5 and added '\n' it does no
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstTbl = row.strip().split('\n')
            print(lstTbl)  # while this does load and print correctly i cant seem to get it to be persitent in memory
            objFile.close
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter a CD id: ')
        strTitle = input('Enter the Title of the CD: ')    # User data taken and then put into dictionary and appended into dicRow list.
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id':intID, 'Title': strTitle,'Artist': strArtist}
        lstTbl.append(dicRow)
        
        
    elif strChoice == 'i': # No need to change from Starter
       print('Current Inventory')
       for row in lstTbl:
            print(row, sep = ',') 
            
            
    elif strChoice == 'd':
        del_id = int(input('Enter Desired CD ID to remove:')) # user input ID selection 
        for intID, value in dict(dicRow).items(): # searching in dicRow for del_id then matching with key value "intId"
            if value == del_id: # if the value equals the user inputed selection 
             dicRow.clear() #Program clears the entry 
             
        
    elif strChoice == 's': # Save function to file 
        objFile = open(strFileName, 'a')
        objFile.write(str(lstTbl)+'\n')
        objFile.close()
else:
    print('Please choose either l, a, i, d, s or x!')

