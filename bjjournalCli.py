#!/usr/bin/env python3

import sys
import os
import re
import glob
from colorama import init, deinit, Fore, Back, Style
#for clearing terminal in Windows and Unix too
os.system('cls' if os.name == 'nt' else 'clear')

class BG:
    purple='\033[45m'
    brown='\ '


init()

# function to convert a list to string 
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1

def makeFilename(text, mode):
    ##This function makes the string strictly alphanumeric except the character specified by the variable 'pop', thus ok for a filename.
    
    #This is used for replacing special chars in dates in filenames
    if mode == 0 : 
        pop = '_'
    #This, for hours
    else:
        pop = '.'

    text = re.sub('[^A-Za-z0-9]+', pop , text)
    return text


def checkAndFormatBeltColor(color_str):
    #Checks the belt color name and formats it properly in case it is messed up, because it is important
    
    if color_str.lower() == 'white':
        color_str = 'White'
    
    elif color_str.lower() == 'blue':
        color_str = 'Blue'
    
    elif color_str.lower() == 'purple':
        color_str = 'Purple'

    elif color_str.lower() == 'brown':
        color_str = 'Brown'
    
    elif color_str.lower() == 'black':
        color_str = 'Black'

    else:
        color_str = input(Style.RESET_ALL +Fore.GREEN +'║ ' + Fore.BLUE + 'NEW PROFILE ' + Fore.GREEN + ' ╟──┼─What color of belt do you have?' + Fore.RED + '(Input a valid color!)' + Fore.GREEN + ' -> ' + Style.RESET_ALL + Fore.CYAN)
        color_str = checkAndFormatBeltColor(color_str)

    return color_str

def getInfo():

    print(Fore.YELLOW + '\n** ADDING NEW USER PROFILE' + Style.RESET_ALL)

    newName = input(Fore.GREEN + '                  ╭─What\'s your name? -> ' + Style.RESET_ALL + Fore.CYAN)
    
    newClub = input(Style.RESET_ALL +Fore.GREEN + '╔══════════════╗  ├─What is the name of your club -> ' + Style.RESET_ALL + Fore.CYAN)
    
    newBelt = input(Style.RESET_ALL +Fore.GREEN +'║ ' + Fore.BLUE + 'NEW PROFILE ' + Fore.GREEN + ' ╟──┼─What color of belt do you have? -> ' + Style.RESET_ALL + Fore.CYAN)
    newBelt = checkAndFormatBeltColor(newBelt)
    
    newStripes = input(Style.RESET_ALL +Fore.GREEN +'╚══════════════╝  ├─How many stripes do you have? -> ' + Style.RESET_ALL + Fore.CYAN)
    newAchievements = input(Style.RESET_ALL + Fore.GREEN +'                  ╰─Any additional notes/achievements (Championships etc.) -> ' + Style.RESET_ALL + Fore.CYAN)

    with open('info/userInfo', 'w') as f:
        print("++++ PROFILE INFO ++++\n" + 'Name: ' + newName + '\nClub: ' + newClub + '\nBelt: ' +  newBelt + '\nStripes: ' + newStripes + '\nAchievements: ' + newAchievements, file=f)


def printBelt(config):
    #if the opening of the file fails, this is not executed and the function is called again (see 'except OSerror' section 5 lines up)
    print(Fore.GREEN + '*' + Style.RESET_ALL + ' Config loaded!')
    file_contents = config.read()

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


def printTotalTime():

    
    try:
        journalPath = glob.glob("journalEntries/*")
        if journalPath == None:
            raise OSError
        
        time = 0
        
        for journal in journalPath:
            journal=open(journal, 'r')
            journal_contents = journal.read()
            if "Duration:" in journal:
                tempTime = re.findall(r'Duration: \d+', journal_contents)
                tempTime = re.findall(r'\d+', tempTime[0])
                time += tempTime

        print(time)
    except OSError:
        print(' !! No journalEntries found!')


def displayAllInfo():
   
    try:
        inf = open('info/userInfo', 'r')
    except OSError:
        print(' !! No Config found! Want to make a new user profile?')
        getInfo()
        displayAllInfo()
    else:
        printBelt(inf)
        printTotalTime()
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
    #Getting multiline input from user
    print(Style.RESET_ALL + Fore.GREEN +'                  ╰─Enter Notes (' + Fore.BLUE + 'Double space to stop taking notes' + Fore.GREEN + '): ' + Style.RESET_ALL + Fore.CYAN)
    newNotes = []

    lineOfNote = "NaN"

    while True:
        if ( lineOfNote != "\n" ):
            lineOfNote = input()
            #Make a new line 
            lineOfNote +="\n"
        else:
            lineOfNote ="-*-"
            newNotes.append(lineOfNote)
            break
        newNotes.append(lineOfNote)

    #making notes into a string to copy to the file
    newNotesStr = listToString(newNotes)

    with open('journalEntries/'+newDate+'_'+newStart, 'w') as f:
        print("Tags: " + newTags, file=f)
        print("Duration: " + newHours + " hours", file=f)
        print("-*- Notes: \n\n" + newNotesStr, file=f)


####Main Program starts here

print(Fore.BLUE + '*** BBJOURNAL ***' + Style.RESET_ALL)


##Making directory for fighter's info, if it exists throw error 

try: 
    os.mkdir('info')
except OSError:
    print(Fore.GREEN + '*' + Style.RESET_ALL + ' Config directory \'info\' found!')
else:
    print('No Config directory found (and thus no \'userInfo\' Config)! Want to make a new user profile?')
    getInfo()

##Making dir for training logs, if it exists throw error

try: 
    os.mkdir('journalEntries')
except OSError:
    print(Fore.GREEN + '*' + Style.RESET_ALL + ' Journal Entries found!')


while 1:

    displayAllInfo()

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

