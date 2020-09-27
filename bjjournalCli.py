#!/usr/bin/env python3

import sys
import os
import re

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def makeFilename(text, mode):
    ##This function makes the string strictly alphanumeric except the character specified by the variable 'pop', thus ok for a filename.
    
    #This is used for replacing special chars in dates in filenames
    if mode == 0 : 
        pop = '_'
    #This, for hours
    else:
        pop = '.'

    text = re.sub('[^A-Za-z0-9]+', pop , text)
    return text;


def printInfo():
    
    inf = open('info/userInfo', 'r')
    file_contents = inf.read()
    print ("\n\n"+file_contents)
    inf.close()


def editInfo():
    
    print(" > Options:\n· Press 1 for full setup\n· Press 2 to edit Name\n· Press 3 to edit Belt Level.\n· Press 4 to edit Dojo/Club.\n· Press 0 to go back.")
    choice = input("Enter your choice here -> ")
    
    if choice == '1':
        addNew()
    if choice == '2':
        editInfo()


def addNew():

    print(bcolors.GREEN + '** ADDING NEW TRAINING LOG' + bcolors.ENDC)
    
    print(bcolors.BOLD)
    newDate = makeFilename( input('Enter date of training session ->'), 0)
    newStart = makeFilename( input('Enter the time it started ->'), 1)
    newHours = input('Enter duration -> ')
    newTags = input('Enter Tags -> ')
    newNotes = input('Enter Notes -> ')
    print(bcolors.ENDC)
    
    with open('journalEntries/'+newDate+'_'+newStart, 'w') as f:
        print("Tags: " + newTags, file=f)
        print("Duration: " + newHours + " hours", file=f)
        print("Notes: \n" + newNotes, file=f)


####Main Program starts here

print(bcolors.BLUE + '*** BBJOURNAL ***' + bcolors.ENDC)


##Making directory for fighter's info, if it exists throw error 

try: 
    os.mkdir('info')
except OSError:
    print(bcolors.GREEN + '*' + bcolors.ENDC + ' Config loaded!')
else:
    with open('info/userInfo', 'w') as f:
        print("++++ PROFILE INFO ++++", file=f)

##Making dir for training logs, if it exists throw error

try: 
    os.mkdir('journalEntries')
except OSError:
    print(bcolors.GREEN + '*' + bcolors.ENDC + ' Journal Entries found!')


while 1:

    printInfo()

    print(" > Options:\n· Press 1 to add a new training log\n· Press 2 for editing your profile info\n· Press 0 to exit.")
    choice = input("Enter your choice here -> ")
    
    if choice == '1':
        addNew()
        break
    if choice == '2':
        editInfo()
        break
    if choice == '0':
        print("\nBye :)\n\n")
        sys.exit()

    print(bcolors.FAIL + 'Please enter a valid value' + bcolors.ENDC)




