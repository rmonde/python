''' This is a note taking program'''
import os

while True: 
    fileName = input('Please enter file name: ')
    if fileName:
        break
    else:
        print('File name can not be blank')

try:
    myFile = open(fileName,"r")
    myFile.close()
    while True:
        choice = input('Please let us know your choice: a) Read the content b)Delete the file and start over c)  Append the file d)Replace the content\n')
        if choice.lower() == "a":
            myFile = open(fileName,"r")
            textToRead = myFile.read()
            print('Here is file content')
            print('------------------------')
            print(textToRead)
            myFile.close()
            break
        elif choice.lower() == "b":
            if os.path.exists(fileName):
                os.remove(fileName)
            else:
                print('Unable to find the file to delte.Please recheck the file name')
            textToWrite = input('Please enter text to write in this file\n')
            myFile = open(fileName,"w")
            myFile.write(textToWrite)
            print('File writing completed')
            myFile.close()
            break
        elif choice.lower() == "c":
            myFile = open(fileName,"a")
            textToWrite = input('Please enter text to write in this file\n')
            myFile = open(fileName,"a")
            myFile.write('\n')
            myFile.write(textToWrite)
            myFile.close()
            print('Added the given to the file')
            break
        elif choice.lower() == 'd':
            while True:
                try:
                    lineNumber = int(input('Please enter line number to replace the text in the file\n'))
                    break
                except ValueError:
                    print('Oops..You seems to have entered incorrect value for line number')
            textToReplace = input('Please enter text to replace in the file\n')
            myFile = open(fileName,'r+')
            lineToDelete = myFile.seek(lineNumber)
            
        else:
            print('Invalid choide. Please enter either a or b or c')
except IOError:
    textToWrite = input('Please enter text to write in this file\n')
    myFile = open(fileName,"w")
    myFile.write(textToWrite)
    myFile.close()
    print('File writing completed.Thank you')