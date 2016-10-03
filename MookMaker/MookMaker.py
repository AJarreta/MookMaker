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
'''from MookMaker import Main\MookMaker\ListsSource.txt'''

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
        print "2. Save the character."
        print "3. Load a stored character."
        print "4. Print the character."
        print "5. Settings."
        print "6. Exit."
        UserResponse = int(raw_input("Choose an option: "))
    except ValueError:
        cls()
        print "That is not an available option."
    else:
        if UserResponse == 1:
            cls()
            print "-------------------"
            print " CHARACTER CLASSES"
            print "-------------------"
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