import random
import charclass
import os
import json

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

SourceFile = open("DataSource.json", "r")
RandomDataSource = json.load(SourceFile)
SourceFile.close()

DefaultDirPath = os.getcwd() + "\MookChars"
CurrentDirPath = DefaultDirPath

while True:
    try:
        os.mkdir(DefaultDirPath)
    except OSError:
        break
        
ValidInputYes = ['y', 'Y', 'yes', 'Yes', 'YES']
ValidInputNo = ['n', 'N', 'no', 'No', 'NO']
ValidInputBack = ['back', 'Back', 'b', 'B', 'BACK']
ValidInputReset = ['reset', 'Reset', 'r', 'R', 'RESET']

#--------------------
#STATUS TRACKER: Variable that- wait for it- tracks whether the user has a character created or not, and under which conditions.
#Possible values:
#0: Starting value; first use, user has not created any character
#1: User has used CharacterGenerator; a character is stored
#2: User has no characters, but after first use (e.g. after resetting character)
#--------------------

StatusTracker = 0

UserCharacter = charclass.CthulhuCharacter(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], RandomDataSource["MaleNames"], \
                                           RandomDataSource["Surnames"], RandomDataSource["Nationalities"], RandomDataSource["Languages"], \
                                           RandomDataSource["Arts"])

print "\nWelcome to MookMaker, the random character generator for The Call of Cthulhu!\n"
while True:
    if StatusTracker == 1:
        print "\nYou have created a %s-class character.\n" % UserCharacterClass
    print "------"
    print " MENU"
    print "------\n"
    print "1. Generate a random character."
    print "2. Show last generated character."
    print "3. Delete last generated character."
    print "4. Save the character in a text file."
    print "5. Load a character from a file. (IN DEVELOPMENT)"
    print "6. Print the character. (IN DEVELOPMENT)"
    print "7. Settings. (IN DEVELOPMENT)"
    print "8. Exit.\n"
    print "Choose an option:"
    try:
        UserResponse = int(raw_input(">"))
    except ValueError:
        cls()
        print "There has been some sort of mistake. Please try again."
    else:
        if UserResponse == 1:
            cls()
            while True:
                try:
                    print "-------------------"
                    print " CHARACTER CLASSES"
                    print "-------------------\n"
                    print str('1.').rjust(3), str('Antiquarian').ljust(20), str('2.').rjust(3), str('Athlete').ljust(20), str('3.').rjust(3), str('College Professor').ljust(20)
                    print str('4.').rjust(3), str('Dilettante').ljust(20), str('5.').rjust(3), str('Doctor').ljust(20), str('6.').rjust(3), str('Drifter').ljust(20)
                    print str('7.').rjust(3), str('Farmer').ljust(20), str('8.').rjust(3), str('Journalist').ljust(20), str('9.').rjust(3), str('Gangster').ljust(20) 
                    print str('10.').rjust(3), str('Lawyer').ljust(20), str('11.').rjust(3), str('Missionary').ljust(20), str('12.').rjust(3), str('Parapsychologist').ljust(20)
                    print str('13.').rjust(3), str('Police').ljust(20), str('14.').rjust(3), str('Politician').ljust(20), str('15.').rjust(3), str('Private Detective').ljust(20)
                    print str('16.').rjust(3), str('Revolutionary').ljust(20), str('17.').rjust(3), str('Soldier').ljust(20), str('18.').rjust(3), str('Writer').ljust(20)
                    print "19. Back\n"
                    print "Choose an option:"
                    UserResponse = int(raw_input(">"))
                except ValueError:
                    cls()
                    print "There has been some sort of mistake. Please try again."
                else:
                    if not UserResponse in range(1, 19):
                        cls()
                        print "There has been some sort of mistake. Please try again."
                    if UserResponse == 19:
                        cls()
                        break
                    if StatusTracker == 1:
                        print "You have already created a character. Do you want to overwrite it? (y/n):"
                        while True:
                            UserInput = raw_input(">")
                            if UserInput in ValidInputYes:
                                StatusTracker = 2
                                break
                            elif UserInput in ValidInputNo:
                                cls()
                                break
                            else:
                                print "\nThere has been some sort of mistake. Please try again.\n"
                    if StatusTracker == 0 or StatusTracker == 2:
                        cls()
                        UserCharacter.ResetCharacter()
                        if UserResponse == 1:
                            UserCharacter = charclass.Antiquarian(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Antiquarian"
                        elif UserResponse == 2:
                            UserCharacter = charclass.Athlete(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Athlete"
                        elif UserResponse == 3:
                            UserCharacter = charclass.CollegeProfessor(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "College Professor"
                        elif UserResponse == 4:
                            UserCharacter = charclass.Dilettante(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Dilettante"
                        elif UserResponse == 5:
                            UserCharacter = charclass.Doctor(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Doctor"
                        elif UserResponse == 6:
                            UserCharacter = charclass.Drifter(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Drifter"
                        elif UserResponse == 7:
                            UserCharacter = charclass.Farmer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Farmer"
                        elif UserResponse == 8:
                            UserCharacter = charclass.Journalist(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Journalist"
                        elif UserResponse == 9:
                            UserCharacter = charclass.Gangster(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Gangster"
                        elif UserResponse == 10:
                            UserCharacter = charclass.Lawyer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Lawyer"
                        elif UserResponse == 11:
                            UserCharacter = charclass.Missionary(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Missionary"
                        elif UserResponse == 12:
                            UserCharacter = charclass.Parapsychologist(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Parapsychologist"
                        elif UserResponse == 13:
                            UserCharacter = charclass.Police(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Police"
                        elif UserResponse == 14:
                            UserCharacter = charclass.Politician(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Politician"
                        elif UserResponse == 15:
                            UserCharacter = charclass.PrivateInvestigator(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Private Investigator"
                        elif UserResponse == 16:
                            UserCharacter = charclass.Revolutionary(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Revolutionary"
                        elif UserResponse == 17:
                            UserCharacter = charclass.Soldier(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Soldier"
                        elif UserResponse == 18:
                            UserCharacter = charclass.Writer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacterClass = "Writer"
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        StatusTracker = 1
                        os.system('pause')
                        cls()
                    else:
                        cls()
                        break  
        elif UserResponse == 2:
            cls()
            if StatusTracker == 0:
                print "\nYou have not created any characters yet.\n"
            elif StatusTracker == 2:
                print "\nYou have currently no created characters.\n"
            else:
                UserCharacter.PrintCharacter()
                os.system('pause')
                cls()

        elif UserResponse == 3:
            cls()
            if StatusTracker == 0:
                print "\nYou have not created any characters yet.\n"
            elif StatusTracker == 2:
                print "\nYou have currently no created characters.\n"
            else:
                while True:
                    UserInput = raw_input("\nAre you sure you want to delete the current character? (yes/ no):")
                    if not UserInput in ValidInputYes and not UserInput in ValidInputNo:
                        cls()
                        print "There has been some sort of mistake. Please try again."
                    else:
                        if UserInput in ValidInputYes:
                            cls()
                            UserCharacter.ResetCharacter()
                            StatusTracker == 2
                            print "The character you created has been deleted."
                            os.system('pause')
                            break
                        else:
                            cls()
                            break

# --------------------------------------------------------
# IN DEVELOPMENT
# To complete:
# -Setting the method to change the working directory
# --------------------------------------------------------

        elif UserResponse == 4:
            cls()
            if StatusTracker == 0:
                print "\nYou have not created any characters yet.\n"
            elif StatusTracker == 2:
                print "\nYou have currently no created characters.\n"
            else:
                while True:
                    try:
                        print "-------------------"
                        print " SAVE A CHARACTER"
                        print "-------------------"
                        print "The character will be saved in:", CurrentDirPath
                        print "1. Change the directory path"
                        print "2. Save the character"
                        print "3. Back"
                        print "Choose an option: "
                        UserResponse = int(raw_input(">"))
                    except ValueError:
                            cls()
                            print "There has been some sort of mistake. Please try again."
                    else:
                        if UserResponse == 1:
                            print "\nPlease introduce the new folder below."
                            print "Introduce the complete directory path, following the formula: C:\\<folder>\\...\\<folder>. This will only work with existing folders"
                            print "If you wish to go back, type \"back\". If you wish to reset the current path to the default path, type \"reset\"."
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputBack:
                                    cls()
                                    break
                                elif UserInput in ValidInputReset:
                                    CurrentDirPath = DefaultDirPath
                                    print "The working directory has been reset to", DefaultDirPath
                                    os.system('pause')
                                    cls()
                                    break
                                elif os.path.isdir(UserInput) == True:
                                    if os.access(UserInput, os.W_OK) == False:
                                        print "You don't have permission to save a file in that folder. Please try another one."
                                    else:
                                        CurrentDirPath = UserInput
                                        print "The working directory has been set to", CurrentDirPath
                                        os.system('pause')
                                        cls()
                                        break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        elif UserResponse == 2:
                            while True:
                                UserInput = raw_input("Are you sure you want to save the current character in this folder? (yes/ no):")
                                if not UserInput in ValidInputYes and not UserInput in ValidInputNo:
                                    cls()
                                    print "There has been some sort of mistake. Please try again."
                                else:
                                    if UserInput in ValidInputYes:
                                        if CurrentDirPath.endswith('\\') == True:
                                            CurrentDirPath = CurrentDirPath[:-1]
                                        CharPrintFileName = CurrentDirPath + "\\" + UserCharacter.CharPersonal["Name"] + ".txt"
                                        CharJSOnFileName = CurrentDirPath + "\\" + UserCharacter.CharPersonal["Name"] + ".json"
                                        DefaultPrint = DefaultDirPath + "\\" + UserCharacter.CharPersonal["Name"] + ".txt"
                                        DefaultJSON =  DefaultDirPath + "\\" + UserCharacter.CharPersonal["Name"] + ".json"
                                        print CharPrintFileName, CharJSOnFileName
                                        print Defaultprint, DefaultJSON
                                        os.system('pause')
                                        NewCharFile = open(CharPrintFileName, "w")
                                        NewJSONFile = open(CharJSOnFileName, "w")
                                        UserCharacter.SaveCharacterInPrintFile(NewCharFile)
                                        UserCharacter.SaveCharacterInJSON(NewJSONFile)
                                        NewCharFile.close()
                                        NewJSONFile.close()
                                        cls()
                                        break
                                    else:
                                        cls()
                                        break
                        elif UserResponse == 3:
                            cls()
                            break
                        else:
                            cls()
                            print "\nThat is not an available option\n"
#--------------------
# IN DEVELOPMENT
# -Build submenu
# -Add methods for
#   1)Add and change working folder
#   3)Select file from folder
#   4)Read file
#   5)Turn raw input from file into data to fill a UserCharacter object with
# -Handling exceptions
#--------------------
        elif UserResponse == 5:
            cls()
            while True:
                try:
                    print "-------------------"
                    print " LOAD A CHARACTER"
                    print "-------------------"
                    print "The character will be loaded from:", CurrentDirPath
                    print "1. Change the directory path"
                    print "2. Load the character"
                    print "3. Back"
                    UserInput = int(raw_input("Choose an option:"))
                except ValueError:
                    print "There has been some sort of mistake. Please try again."
                else:
                    if UserInput == 1:
                            print "\nPlease introduce the new folder below."
                            print "Introduce the complete directory path, following the formula: C:\\<folder>\\...\\<folder>. This will only work with existing folders"
                            print "If you wish to go back, type \"back\". If you wish to reset the current path to the default path, type \"reset\"."
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputBack:
                                    cls()
                                    break
                                elif UserInput in ValidInputReset:
                                    CurrentDirPath = DefaultDirPath
                                    print "The working directory has been reset to", DefaultDirPath
                                    os.system('pause')
                                    cls()
                                    break
                                elif os.path.isdir(UserInput) == True:
                                    if os.access(UserInput, os.R_OK) == False:
                                        print "You don't have permission to load a file from that folder. Please try another one."
                                    else:
                                        CurrentDirPath = UserInput
                                        print "The working directory has been set to", CurrentDirPath
                                        os.system('pause')
                                        cls()
                                        break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                    elif UserInput == 2:
                        cls()
                        CurrentFiles = os.listdir(CurrentDirPath)
                        print "The files in the current working directory are:"
                        x = 0
                        for files in CurrentFiles:
                            print CurrentFiles[x], "\n"
                            x += 1
                        print "Which file do you desire to load? (Type \"back\" to return to the previous menu)"
                        while True:
                            try:
                                UserResponse = raw_input(">")
                                if UserResponse in ValidInputBack:
                                    cls()
                                    break
                                elif not UserResponse in CurrentFiles:
                                    print "There has been some sort of mistake. Please try again."
                                else:
                                    CharJSOnFileName = CurrentDirPath + "\\" + UserResponse
                                    NewJSONFile = open(CharJSOnFileName, "r")
                                    CharClass = json.loads(NewJSONFile[CharPersonal[Profession]])
                                    print CharClass
                                    if CharClass == "Antiquarian":
                                        UserCharacter = charclass.Antiquarian.CharacterGenerator
                                    elif CharClass == "Athlete":
                                        UserCharacter = charclass.Athlete.CharacterGenerator
                                    elif CharClass == "College Professor":
                                        UserCharacter = charclass.CollegeProfessor.CharacterGenerator
                                    elif CharClass == "Dilettante":
                                        UserCharacter = charclass.Dilettante.CharacterGenerator
                                    elif CharClass == "Doctor":
                                        UserCharacter = charclass.Doctor.CharacterGenerator 
                                    elif CharClass == "Drifter":
                                        UserCharacter = charclass.Drifter.CharacterGenerator
                                    elif CharClass == "Farmer":
                                        UserCharacter = charclass.Farmer.CharacterGenerator
                                    elif CharClass == "Gangster":
                                        UserCharacter = charclass.Gangster.CharacterGenerator 
                                    elif CharClass == "Journalist":
                                        UserCharacter = charclass.Journalist.CharacterGenerator  
                                    elif CharClass == "Lawyer":
                                        UserCharacter = charclass.Lawyer.CharacterGenerator   
                                    elif CharClass == "Missionary":
                                        UserCharacter = charclass.Missionary.CharacterGenerator
                                    elif CharClass == "Parapsychologist":
                                        UserCharacter = charclass.Parapsychologist.CharacterGenerator
                                    elif CharClass == "Police":
                                        UserCharacter = charclass.Police.CharacterGenerator
                                    elif CharClass == "Politician":
                                        UserCharacter = charclass.Politician.CharacterGenerator
                                    elif CharClass == "Private Investigator":
                                        UserCharacter = charclass.PrivateInvestigator.CharacterGenerator
                                    elif CharClass == "Revolutionary":
                                        UserCharacter = charclass.Revolutionary.CharacterGenerator
                                    elif CharClass == "Soldier":
                                        UserCharacter = charclass.Soldier.CharacterGenerator
                                    elif CharClass == "Writer":
                                        UserCharacter = charclass.Writer.CharacterGenerator
                                    else:
# Maybe force a ValueError to cause a loop?
                                        pass 
                                    UserCharacter.ReadCharacterfromFile(NewJSONFile)
                                    UserCharacter.PrintCharacter()
                                    os.system('pause')
                            except ValueError:
                                print "There has been some sort of mistake. Please try again."                             
                    elif UserInput == 3:
                        cls()
                        break
                    else:
                        print "There has been some sort of mistake. Please try again."
                        
            pass
#--------------------
# IN DEVELOPMENT
# -Build submenu
# -Add methods for
#   1)Add and change target character file
#   3)Select printer from system
#   4)Turn file into data accepted by the printer
#   5)Print the file
# -Handling exceptions
#--------------------
        elif UserResponse == 6:
            cls()
            pass
        elif UserResponse == 7:
            cls()
            pass
        elif UserResponse == 8:
            break
        else:
            cls()
            print "That is not an available option."
