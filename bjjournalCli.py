#!/usr/bin/env python3

import sys
import os

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printInfo():
    
    inf = open('info/userInfo', 'r')
    file_contents = inf.read()
    print (file_contents)
    inf.close()


def addNew():

    print(bcolors.GREEN + '** ADDING NEW TRAINING LOG' + bcolors.ENDC)
    
    print(bcolors.BOLD)
    newDate = input('Enter date of training session ->')
    newHours = input('Enter duration (in hours) -> ')
    newTags = input('Enter Tags -> ')
    newNotes = input('Enter Notes -> ')
    print(bcolors.ENDC)
    
    with open('testfolder/'+newDate, 'w') as f:
        print("Tags: " + newTags, file=f)
        print("Duration: " + newHours + " hours", file=f)
        print("Notes: \n" + newNotes, file=f)


####Main Program starts here

print(bcolors.BLUE + '*** BBJOURNAL ***' + bcolors.ENDC)

try: 
    os.mkdir('info')
except OSError:
    print(bcolors.GREEN + '*' + bcolors.ENDC + ' Config loaded!')
else:
    with open('info/userInfo', 'w') as f:
        print("Belt: White", file=f)


while 1:

    printInfo()

    print(" > Options:\n· Press 1 to add a new training log\n· Press 2 for View dialog\n· Press 0 to exit.")
    choice = input("Enter your choice here -> ")
    
    if choice == '1':
        addNew()
        break
    
    print(bcolors.FAIL + 'Please enter a valid value' + bcolors.ENDC)




