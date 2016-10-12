import random
import charclass
import os
import json

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

SourceFile = open("DataSource.json", "r")
RandomDataSource = json.load(SourceFile)
SourceFile.close()

UserCharacter = charclass.CthulhuCharacter(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], RandomDataSource["MaleNames"], \
                                           RandomDataSource["Surnames"], RandomDataSource["Nationalities"], RandomDataSource["Languages"], \
                                           RandomDataSource["Arts"])

while True:
    try:
        print "Welcome to MookMaker, the random character generator for The Call of Cthulhu!"
        print "------"
        print " MENU"
        print "------"
        print "1. Generate a random character."
        print "2. Show last generated character."
        print "3. Delete last generated character."
        print "4. Save the character in a text file."
        print "5. Load a character from a file."
        print "6. Print the character."
        print "7. Settings."
        print "8. Exit."
        UserResponse = int(raw_input("Choose an option: "))
    except ValueError:
        cls()
        print "That is not an available option."
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
                    print "That is not an available option."
                else:
                    if UserResponse == 1:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Antiquarian(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 2:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Athlete(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 3:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.CollegeProfessor(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 4:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Dilettante(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 5:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Doctor(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 6:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Drifter(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 7:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Farmer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 8:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Journalist(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 9:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Gangster(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 10:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Lawyer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 11:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Missionary(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 12:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Parapsychologist(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 13:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Police(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 14:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Politician(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 15:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.PrivateInvestigator(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 16:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Revolutionary(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 17:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Soldier(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 18:
                        cls()
                        UserCharacter.ResetCharacter()
                        UserCharacter = charclass.Writer(RandomDataSource["Nationalities"], RandomDataSource["FemaleNames"], \
                                        RandomDataSource["MaleNames"], RandomDataSource["Surnames"], RandomDataSource["Nationalities"], \
                                        RandomDataSource["Languages"], RandomDataSource["Arts"])
                        UserCharacter.CharacterGenerator()
                        UserCharacter.PrintCharacter()
                        os.system('pause')
                    elif UserResponse == 19:
                        cls()
                        break
                    else:
                        cls()
                        print "That is not an available option."
                        pass    
        elif UserResponse == 2:
            cls()
            pass
        elif UserResponse == 3:
            cls()
            pass
        elif UserResponse == 4:
            cls()
            pass
        elif UserResponse == 5:
            cls()
            pass
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