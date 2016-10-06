'''import random

AverageComposite = 0

for x in range(10000):
    
    AverageComposite += result

AverageResult = float(AverageComposite/10000)

print AverageResult

'''

import random
import charclass
import os
import json

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

SourceFile = open("ListsSource.txt", "r")
SourceFile.close()

while True:
    try:
        print "Welcome to MookMaker, the random character generator for The Call of Cthulhu RPG!"
        print "------"
        print " MENU"
        print "------"
        print "1. Generate a random character."
        print "2. Show last generated character."
        print "3. Save the character."
        print "4. Load a stored character."
        print "5. Print the character."
        print "6. Settings."
        print "7. Exit."
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
                    print "1. Antiquarian.\t2. Athlete.\t3. College Professor.\t\t4. Dilettante.\t\t5. Doctor.\t6. Drifter."
                    print "7. Farmer.\t8. Journalist.\t9. Gangster.\t\t\t10. Lawyer.\t\t11. Missionary.\t12. Parapsychologist"
                    print "13. Police.\t14. Politician.\t15. Private Investigator.\t16. Revolutionary.\t17. Soldier.\t18. Writer."
                    print "19. Back"
                    UserResponse = int(raw_input("Choose an option: "))
                except ValueError:
                    cls()
                    print "That is not an available option."
                else:
                    if UserResponse == 1:
                        cls()
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
                        cls()
                        pass
                    elif UserResponse == 9:
                        cls()
                        pass
                    elif UserResponse == 10:
                        cls()
                        pass
                    elif UserResponse == 11:
                        cls()
                        pass
                    elif UserResponse == 12:
                        cls()
                        pass
                    elif UserResponse == 13:
                        cls()
                        pass
                    elif UserResponse == 14:
                        cls()
                        pass
                    elif UserResponse == 15:
                        cls()
                        pass
                    elif UserResponse == 16:
                        cls()
                        pass
                    elif UserResponse == 17:
                        cls()
                        pass
                    elif UserResponse == 18:
                        cls()
                        pass
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
            break
        else:
            cls()
            print "That is not an available option."

'''
TestLawyer = charclass.Lawyer()

TestLawyer.LawyerGenerator()

print TestLawyer.CharStats

print TestLawyer.CharDerivedStats

print TestLawyer.ClassSkills

print TestLawyer.CharSkills

print TestLawyer.CharCombatSkills

print TestLawyer.PersonalGeneration
'''