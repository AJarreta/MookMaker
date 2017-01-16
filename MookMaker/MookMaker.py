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
ResetSwitch = False

UserCharacter = charclass.CthulhuCharacter(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], RandomDataSource["MaleNames"], \
                                           RandomDataSource["Surnames"], RandomDataSource["Nationalities"], RandomDataSource["Languages"], \
                                           RandomDataSource["Arts"])

while True:
    try:
        print "Welcome to MookMaker, the random character generator for The Call of Cthulhu!"
# add conditional "If" to warn the user there is a created character
        if type(UserCharacter) != charclass.CthulhuCharacter:
            print "You have created a %s-class character." % UserCharacterClass
        print "------"
        print " MENU"
        print "------"
        print "1. Generate a random character."
        print "2. Show last generated character."
        print "3. Delete last generated character."
        print "4. Save the character in a text file."
        print "5. Load a character from a file. (IN DEVELOPMENT)"
        print "6. Print the character. (IN DEVELOPMENT)"
        print "7. Settings. (IN DEVELOPMENT)"
        print "8. Exit."
        UserResponse = int(raw_input("Choose an option: "))
    except ValueError:
        cls()
        print "There has been some sort of mistake. Please try again."
    else:
        if UserResponse == 1:
            while True:
                try:
                    cls()
                    print "-------------------"
                    print " CHARACTER CLASSES"
                    print "-------------------"
                    print str('1.').rjust(3), str('Antiquarian').ljust(20), str('2.').rjust(3), str('Athlete').ljust(20), str('3.').rjust(3), str('College Professor').ljust(20)
                    print str('4.').rjust(3), str('Dilettante').ljust(20), str('5.').rjust(3), str('Doctor').ljust(20), str('6.').rjust(3), str('Drifter').ljust(20)
                    print str('7.').rjust(3), str('Farmer').ljust(20), str('8.').rjust(3), str('Journalist').ljust(20), str('9.').rjust(3), str('Gangster').ljust(20) 
                    print str('10.').rjust(3), str('Lawyer').ljust(20), str('11.').rjust(3), str('Missionary').ljust(20), str('12.').rjust(3), str('Parapsychologist').ljust(20)
                    print str('13.').rjust(3), str('Police').ljust(20), str('14.').rjust(3), str('Politician').ljust(20), str('15.').rjust(3), str('Private Detective').ljust(20)
                    print str('16.').rjust(3), str('Revolutionary').ljust(20), str('17.').rjust(3), str('Soldier').ljust(20), str('18.').rjust(3), str('Writer').ljust(20)
                    print "19. Back"
                    UserResponse = int(raw_input("Choose an option: "))
                except ValueError:
                    cls()
                    print "There has been some sort of mistake. Please try again."
                else:
                    if UserResponse == 1:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Antiquarian(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Antiquarian"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 2:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Athlete(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Athlete"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 3:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.CollegeProfessor(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "College Professor"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 4:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Dilettante(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Dilettante"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 5:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Doctor(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Doctor"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 6:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Drifter(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Drifter"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 7:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Farmer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Farmer"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 8:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Journalist(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Journalist"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 9:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Gangster(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Gangster"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 10:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Lawyer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Lawyer"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 11:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Missionary(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Missionary"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 12:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Parapsychologist(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Parapsychologist"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 13:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Police(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Police"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 14:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Politician(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Politician"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 15:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.PrivateInvestigator(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Private Investigator"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 16:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Revolutionary(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Revolutionary"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 17:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Soldier(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Soldier"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 18:
                        if type(UserCharacter) != charclass.CthulhuCharacter:
                            print "You have already created a character. Do you want to overwrite it? (y/n):"
                            while True:
                                UserInput = raw_input(">")
                                if UserInput in ValidInputYes:
                                    SwitchMenuOption = 1
                                    break
                                elif UserInput in ValidInputNo:
                                    SwitchMenuOption = 0
                                    cls()
                                    break
                                else:
                                    print "There has been some sort of mistake. Please try again."
                        else:
                            SwitchMenuOption = 1
                        if SwitchMenuOption == 1:
                            cls()
                            UserCharacter.ResetCharacter()
                            UserCharacter = charclass.Writer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                            UserCharacter.CharacterGenerator()
                            UserCharacter.PrintCharacter()
                            UserCharacterClass = "Writer"
                            ResetSwitch = False
                            os.system('pause')
                        else:
                            break
                    elif UserResponse == 19:
                        cls()
                        break
                    else:
                        cls()
                        print "That is not an available option."
                        pass    
        elif UserResponse == 2:
            cls()
            if type(UserCharacter) == charclass.CthulhuCharacter:
                print "\nYou have not created any characters yet.\n"
            elif ResetSwitch == True:
                print "\nYou have currently no created characters.\n"
            else:
                UserCharacter.PrintCharacter()
                os.system('pause')
                cls()
        elif UserResponse == 3:
            cls()
            if type(UserCharacter) == charclass.CthulhuCharacter:
                print "\nYou have not created any characters yet.\n"
            elif ResetSwitch == True:
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
                            ResetSwitch = True
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
            if type(UserCharacter) == charclass.CthulhuCharacter:
                print "\nYou have not created any characters yet.\n"
            elif ResetSwitch == True:
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
                        UserResponse = int(raw_input("Choose an option: "))
                    except ValueError:
                        print "There has been some sort of mistake. Please try again."
                    else:
                        if UserResponse == 1:
                            while True:
                                print "\nPlease introduce the new folder below."
                                print "Introduce the complete directory path, following the formula: C:\\<folder>\\...\\<folder>. This will only work with existing folders"
                                print "If you wish to go back, type \"back\". If you wish to reset the current path to the default path, type \"reset\"."
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
                                elif os.path.exists(UserInput) == True:

                                    
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
                                        CharFileName = CurrentDirPath + "\\" + UserCharacter.CharPersonal["Name"] + ".txt"
                                        NewCharFile = open(CharFileName, "w")
                                        UserCharacter.SaveCharacterInFile(NewCharFile)
                                        NewCharFile.close()
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
                           print "That is not an available option"
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
                    UserInput = raw_input("Choose an option:")
                except ValueError:
                    print "There has been some sort of mistake. Please try again."
                else:
                    if UserInput == 1:
                        NewCharFile.re
                        pass
                    elif UserInput == 2:
                        pass
                    elif UserInput == 3:
                        pass
                    else:
                        break
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
