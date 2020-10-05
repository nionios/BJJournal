#!/usr/bin/env python3

import sys
import os
import re
from colorama import init, deinit, Fore, Back, Style
#for clearing terminal in Windows and Unix too
os.system('cls' if os.name == 'nt' else 'clear')

init()

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
    
    print("\n\n")



    if "Belt: White" in file_contents:
        belt_color = Back.WHITE
        letter_color = Fore.BLACK
        stripe_area_color = Back.BLACK

    elif "Belt: Blue" in file_contents:
        belt_color = Back.BLUE 
        letter_color = Fore.WHITE
        stripe_area_color = Back.BLACK
    
    elif "Belt: Purple" in file_contents:
        belt_color = Back.PURPLE 
        letter_color = Fore.WHITE
        stripe_area_color = Back.BLACK
    
    elif "Belt: Brown" in file_contents:
        belt_color = Back.BROWN 
        letter_color = Fore.WHITE
        stripe_area_color = Back.BLACK
    
    elif "Belt: Black" in file_contents:
        belt_color = Back.BLACK 
        letter_color = Fore.WHITE
        stripe_area_color = Back.RED
    

    stripe_no = 0

    #double regex to find out where the stripe info is written and how many stripes are there
    if "Stripes:" in file_contents:
        stripe_no = re.findall(r'Stripes: \d+', file_contents)
        stripe_no = re.findall(r'\d+', stripe_no[0])
        

    name = "Unnamed Grappler" 

    if "Name:" in file_contents:
        name = re.findall(r'Name: .*', file_contents)
        name = re.sub(r'Name: ','', name[0])


    #Printing the belt graphic
    print(belt_color + '   ' + letter_color + name + ' ' + stripe_area_color + '  ', end = '' )

    if stripe_no == '0' :
        print('  ' + Style.RESET_ALL, end = '')
    else:
        for i in range(int(stripe_no[0])) :
            print(belt_color + ' ' + stripe_area_color + ' ', end = '' )
        print(' ' + Style.RESET_ALL)

    inf.close()


def editInfo():
    
    print(" > Options:\n· Press 1 for full setup\n· Press 2 to edit Name\n· Press 3 to edit Belt Level.\n· Press 4 to edit Dojo/Club.\n· Press 0 to go back.")
    choice = input("Enter your choice here -> ")
    
    if choice == '1':
        addNew()
    if choice == '2':
        editInfo()


def addNew():

    print(Fore.YELLOW + '\n** ADDING NEW TRAINING LOG' + Style.RESET_ALL)
    
    newDate = makeFilename( input(Fore.GREEN + '                  ╭─Enter date of training session -> ' + Style.RESET_ALL + Fore.CYAN), 0)
    newStart = makeFilename( input(Style.RESET_ALL +Fore.GREEN + '╔══════════════╗  ├─Enter the time it started -> ' + Style.RESET_ALL + Fore.CYAN), 1)
    newHours = input(Style.RESET_ALL +Fore.GREEN +'║ ' + Fore.BLUE + 'TRAINING LOG' + Fore.GREEN + ' ╟──┼─Enter duration -> ' + Style.RESET_ALL + Fore.CYAN)
    newTags = input(Style.RESET_ALL +Fore.GREEN +'╚══════════════╝  ├─Enter Tags -> ' + Style.RESET_ALL + Fore.CYAN)
    newNotes = input(Style.RESET_ALL + Fore.GREEN +'                  ╰─Enter Notes -> ' + Style.RESET_ALL + Fore.CYAN)
    
    with open('journalEntries/'+newDate+'_'+newStart, 'w') as f:
        print("Tags: " + newTags, file=f)
        print("Duration: " + newHours + " hours", file=f)
        print("Notes: \n" + newNotes, file=f)


####Main Program starts here

print(Fore.BLUE + '*** BBJOURNAL ***' + Style.RESET_ALL)


##Making directory for fighter's info, if it exists throw error 

try: 
    os.mkdir('info')
except OSError:
    print(Fore.GREEN + '*' + Style.RESET_ALL + ' Config loaded!')
else:
    with open('info/userInfo', 'w') as f:
        print("++++ PROFILE INFO ++++", file=f)

##Making dir for training logs, if it exists throw error

try: 
    os.mkdir('journalEntries')
except OSError:
    print(Fore.GREEN + '*' + Style.RESET_ALL + ' Journal Entries found!')


while 1:

    printInfo()

    print(" > Options:\n" + Fore.YELLOW + "·" + Style.RESET_ALL + " Press 1 to add a new training log\n" + Fore.YELLOW + "·" + Style.RESET_ALL + " Press 2 for editing your profile info\n" + Fore.YELLOW + "·" + Style.RESET_ALL + " Press 0 to exit.")
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

    print(Fore.RED + 'Please enter a valid value' + Style.RESET_ALL)


deinit()

