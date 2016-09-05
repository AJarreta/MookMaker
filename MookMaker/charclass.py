class CthulhuCharacter(object):
    CharPersonal = {"Name": '', "Age": 0, "Profession": '', "Titles": '', "Nationality": '', "Gender": '', "Personality": ''}
    CharStats = {"STR": 0, "CON": 0, "SIZ": 0, \
                 "INT": 0, "POW": 0, "DEX": 0, \
                 "APP": 0, "EDU": 0, "SAN": 0}
    CharDerivedStats = {"Dam. Bonus": 0, "HP": 0, "Idea": 0, "Luck": 0, "MP": 0, "Knowledge": 0}
    CharSkills = {"Accounting": 10, "Anthropology": 1, "Archaeology": 1, "Art": 5, "Astronomy": 1, \
                  "Bargain": 5, "Biology": 1, "Chemistry": 1, "Climb": 40, "Conceal": 15, "Craft": 5,\
                  "Credit Rating": 15, "Cthulhu Mythos": 0, "Disguise": 1, "Dodge": 0, "Drive Auto": 20,\
                  "Electric Repair": 10, "Fast Talk": 5, "First Aid": 30, "Geology": 1, "Hide": 10, \
                  "History": 20, "Jump": 25, "Law": 5, "Library Use": 25, "Listen": 25, "Locksmith" : 1, \
                  "Martial Arts": 1, "Mechanical Repair": 20, "Medicine": 5, "Natural History": 10, \
                  "Navigate": 10, "Occult": 5, "Operate Heavy Machinery": 1, "Other Language": 1, \
                  "Own Language": 0, "Persuade": 15, "Pharmacy": 1, "Photography": 10, "Physics": 1, \
                  "Pilot": 1, "Psychoanalysis": 1, "Psychology": 5, "Ride": 5, "Sneak": 10, "Spot Hidden": 25, \
                  "Swim": 25, "Throw": 25, "Track": 10}
    CharCombatSkills = {"Fist": 50, "Grapple": 25, "Headbutt": 10, "Kick": 25, "Axe": 20, "Club": 25, "Dagger": 25, \
                        "Knife": 25, "Rapier": 20, "Sabre": 15, "Sword": 10, "Handgun": 20, "Machine Gun": 15, \
                        "Rifle": 25, "Shotgun": 30, "SMG": 15}
    ClassSkillPoints = 0
    FreeSkillPoints = 0

    def __init__(self):
        self.CharPersonal = CharPersonal
        self.CharStats = CharStats
        self.CharDerivedStats = CharDerivedStats
        self.CharSkills = CharSkills
        self.CharCombatSkills = CharCombatSkills
        self.ClassSkillPoints = ClassSkillPoints
        self.FreeSkillPoints = FreeSkillPoints
        return super(CthulhuCharacter, self).__init__(*args, **kwargs)

    def EDURoll(self):
        result = 0
        for i in range(3):
            dicethrow = random.randint(1, 6)
            result += dicethrow
        result += 3
        return result

    def PercentRoll(self):
        result = random.randint(1, 100) 
        return result
        
    def StatRollNormal(self):
        result = 0
        for i in range(3):
            dicethrow = random.randint(1, 6)
            result += dicethrow
        return result
        
    def StatRollHigh(self):
        result = 0
        minorresult = 6
        for i in range(4):
            dicethrow = random.randint(1, 6)
            result += dicethrow
            if dicethrow < minorrresult:
                minorresult = dicethrow
        result -= mminorresult
        return result

    def StatRollXHigh(self):
        result = 0
        for i in range(2):
            dicethrow = random.randint(1,6)
            result += dicethrow
        result += 6
        return result

    def ResetCharacter(self):
        self.CharPersonal = {"Name": '', "Age": 0, "Profession": '', "Titles": '', "Nationality": '', "Gender": '', "Personality": ''}
        self.CharStats = {"STR": 0, "CON": 0, "SIZ": 0, \
                          "INT": 0, "POW": 0, "DEX": 0, \
                          "APP": 0, "EDU": 0, "SAN": 0}
        self.CharDerivedStats = {"Dam. Bonus": 0, "HP": 0, "Idea": 0, "Luck": 0, "MP": 0, "Knowledge": 0}

class Lawyer(CthulhuCharacter):

class Antiquarian(CthulhuCharacter):

class Parapsychologist(CthulhuCharacter):

class Writer(CthulhuCharacter):

class PrivateInvestigator(CthulhuCharacter):

class Journalist(CthulhuCharacter:

class Dilettante(CthulhuCharacter):

class Doctor(CthulhuCharacter):

class CollegeProfessor(CthulhuCharacter):

class Revolutionary(CthulhuCharacter):

class Farmer(CthulhuCharacter):

class Politician(CthulhuCharacter):

class Athlete(CthulhuCharacter):

class Missionary(CthulhuCharacter):

class Soldier(CthulhuCharacter):

class Gangster(CthulhuCharacter):

class Police(CthulhuCharacter):

class Hobo(CthulhuCharacter):
