'''import random

AverageComposite = 0

for x in range(10000):
    
    AverageComposite += result

AverageResult = float(AverageComposite/10000)

print AverageResult

'''

import random
import charclass
from MookMaker import ListsSource

SourceFile = open("ListsSource.txt", "r")
SourceFile.close()

TestLawyer = charclass.Lawyer()

TestLawyer.LawyerGenerator()

print TestLawyer.CharStats

print TestLawyer.CharDerivedStats

print TestLawyer.ClassSkills

print TestLawyer.CharSkills

print TestLawyer.CharCombatSkills

print TestLawyer.PersonalGeneration
