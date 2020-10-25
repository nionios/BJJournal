#!/usr/bin/env python3

import sys
import os
import re
import glob
import getch
from colorama import init, deinit, Fore, Back, Style
#for clearing terminal in Windows and Unix too
os.system('cls' if os.name == 'nt' else 'clear')

class BG:
    BLACK='\033[48;2;0;0;0m'
    BROWN='\033[48;2;9;67;58m'
    PURPLE='\033[48;2;150;0;120m'
    BLUE='\033[48;2;10;0;88m'
    WHITE='\033[48;2;255;255;255m'


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

def getMultilineInput(lineArray):

    line = "NaN"

    while True:
        if ( line != "> \n" ):
            line = "> " + input()
            #Make a new line 
            line +="\n"
        else:
            lineArray.pop()
            line ="-*-"
            lineArray.append(line)
            break
        lineArray.append(line)

    #making notes into a string to copy to the file
    return listToString(lineArray)

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

def checkAndFormatYN(gi_str):
    

    if gi_str.lower() in ['yes', 'y', 'ye', 'yah', 'ja', 'yeh', 'da']:
        gi_str = "y" 
    elif gi_str.lower() in ['no','n','nope','nah','nein','niet', 'wtf']:
        gi_str = "n"
    else: 
        gi_str = input(Style.RESET_ALL +Fore.RED +' (Invalid Answer) '+ Fore.GREEN +'├─Did you wear a Gi? (y/n) -> ' + Style.RESET_ALL + Fore.CYAN)
        checkAndFormatYN(gi_str)

    return gi_str

def checkAndFormatBeltColor(color_str):
    #Checks the belt color name and formats it properly in case it is messed up, because it is important
    
    if color_str.lower() == 'white':
        color_str = 'White'
    
    elif color_str.lower() == 'blue':
        color_str = 'Blue'
    
    elif color_str.lower() == 'PURPLE':
        color_str = 'PURPLE'

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
    
    print(Style.RESET_ALL + Fore.GREEN +'                  ╰─Any additional notes/achievements (Championships etc, '+ Fore.RED +' press enter twice to stop' + Fore.GREEN + '): ' + Style.RESET_ALL + Fore.CYAN)
    
    newAchievements = []
    newAchievementsStr = getMultilineInput(newAchievements)

    with open('info/userInfo', 'w') as f:
        print("++++ PROFILE INFO ++++\n" + 'Name: ' + newName + '\nClub: ' + newClub + '\nBelt: ' +  newBelt + '\nStripes: ' + newStripes + '\nAchievements:\n' + newAchievementsStr, file=f)


def printBelt(config):
    file_contents = config.read()

    if "Belt: White" in file_contents:
        belt_color = BG.WHITE
        letter_color = Fore.BLACK
        stripe_area_color = BG.BLACK

    elif "Belt: Blue" in file_contents:
        belt_color = BG.BLUE 
        letter_color = Fore.WHITE
        stripe_area_color = BG.BLACK
    
    elif "Belt: Purple" in file_contents:
        belt_color = BG.PURPLE 
        letter_color = Fore.WHITE
        stripe_area_color = BG.BLACK
    
    elif "Belt: Brown" in file_contents:
        belt_color = BG.BROWN 
        letter_color = Fore.WHITE
        stripe_area_color = BG.BLACK
    
    elif "Belt: Black" in file_contents:
        belt_color = BG.BLACK 
        letter_color = Fore.WHITE
        stripe_area_color = Back.RED
    
    else: 
        belt_color = Style.RESET_ALL 
        letter_color = Fore.RED + "(Error reading Belt Color)"
        stripe_area_color = Style.RESET_ALL


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

    for i in range(int(stripe_no[0])) :
        print(BG.WHITE + ' ' + stripe_area_color + ' ', end = '' )
    print(' ' + Style.RESET_ALL)


def printTotalTime():

    
    try:
        journalPath = glob.glob("journalEntries/*")
        if journalPath == None:
            raise OSError
        
        time = 0
        GiTime = 0
        NoGiTime = 0
        
        r = re.compile("Duration: .*")
        r2 = re.compile(r"\*\*\* .*GI TRAINING \*\*\*")

        for journal in journalPath:
            journal=open(journal, 'r')
            journal_contents = journal.readlines()

            journal_contents_dur = list(filter(r.match, journal_contents))
            journal_contents_gi = list(filter(r2.match, journal_contents))

            if journal_contents_dur:
                for i in range(len(journal_contents_dur)):

                    ## For Debugging
                    # print(journal_contents_gi)
                    # print(journal_contents_dur)
                    
                    if journal_contents_gi[0] == "*** NOGI TRAINING ***\n":
                        NoGi = 0
                    else:
                        NoGi = 1

                    tempTime = re.findall(r'Duration: \d+', journal_contents_dur[i])
                    tempTime = re.findall(r'\d+', tempTime[0])
                    tempTime_str=''.join(tempTime)
                    time += int(tempTime_str)
                    
                    if NoGi:
                        NoGiTime += int(tempTime_str)
                    else:
                        GiTime += int(tempTime_str)

        print(Fore.BLUE + "* " + Fore.GREEN + "Total mat time: " + Fore.CYAN + str(time) + Fore.GREEN + " hours!" + Style.RESET_ALL)
        print("├─ "+ Fore.GREEN +" NoGi time: " + Style.RESET_ALL + str(NoGiTime) + Fore.GREEN + " hours" + Style.RESET_ALL)
        print("╰─ "+ Fore.GREEN +" Gi time: " + Style.RESET_ALL + str(GiTime)  + Fore.GREEN + " hours" + Style.RESET_ALL)
        
    except OSError:
        print(' !! No journalEntries found!')


def printClubAndNotes(config):
    
    file_contents = config.read()

    club = re.findall(r'Club:.*', file_contents)
    club = re.sub(r'Club:','', club[0])
    
    print(Fore.GREEN + "Club:" + Fore.BLUE + club + Style.RESET_ALL)
   
    print(Fore.GREEN + "Bio:" + Style.RESET_ALL)

    #re.MULTILINE is important, it is needed for the regex to match the EOF
    ach = re.findall(r'^> .*', file_contents, re.MULTILINE)
    
    for i in range(len(ach)):
        #Remove the '> ' string for display 
        ach[i] = re.sub(r'> ','', ach[i])
        print(Fore.BLUE + ach[i] + Style.RESET_ALL)

def displayAllInfo():
   
    try:
        inf = open('info/userInfo', 'r')
    except OSError:
        print(' !! No Config found! Want to make a new user profile?')
        getInfo()
        displayAllInfo()
    else:
        #if the opening of the file fails, this is not executed and the function is called again (see 'except OSerror' section 5 lines up)
        print(Fore.GREEN + '*' + Style.RESET_ALL + ' Config loaded!')
        printBelt(inf)
        printTotalTime()
        #placing the reader at the start of the file again
        inf.seek(0)
        printClubAndNotes(inf)
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
    newGi = input(Style.RESET_ALL +Fore.GREEN +'                  ├─Did you wear a Gi? (y/n) -> ' + Style.RESET_ALL + Fore.CYAN)
    #Checking and formatting this answer
    newGi = checkAndFormatYN(newGi)
    #Getting multiline input from user
    print(Style.RESET_ALL + Fore.GREEN +'                  ╰─Enter Notes (' + Fore.BLUE + 'Double enter to stop taking notes' + Fore.GREEN + '): ' + Style.RESET_ALL + Fore.CYAN)
    newNotes = []

    newNotesStr = getMultilineInput(newNotes)


    with open('journalEntries/'+newDate+'_'+newStart, 'w') as f:
        if ( newGi == 'n' ):
            print("*** NOGI TRAINING ***", file=f)
        else:
            print("*** GI TRAINING ***", file=f)
        print("Tags: " + newTags, file=f)
        print("Date: " + newDate, file=f)
        print("Duration: " + newHours + " hours", file=f)
        print("-*- Notes: \n\n" + newNotesStr, file=f)


####Main Program starts here

print(Fore.BLUE + '*** BJJOURNAL ***' + Style.RESET_ALL)


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

    print(" > Options:\n" + Fore.YELLOW + "·" + Style.RESET_ALL + " Press " + Fore.YELLOW + "1" + Style.RESET_ALL + " to add a new training log\n" + Fore.YELLOW + "·" + Style.RESET_ALL + " Press " + Fore.YELLOW + "2" + Style.RESET_ALL + " for editing your profile info\n" + Fore.YELLOW + "·" + Style.RESET_ALL + " Press " + Fore.YELLOW + "0" + Style.RESET_ALL + " to exit.")
    #choice = input("Enter your choice here -> ")
    choice = getch.getch()

    if choice == '1':
        addNew()
    elif choice == '2':
        editInfo()
    elif choice == '0':
        print("\nBye :)\n\n")
        sys.exit()
    else:
        print(Fore.RED + 'Please enter a valid value' + Style.RESET_ALL)


deinit()

