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
                  "History": 20, "Jump" 25, "Law": 5, "Library Use": 25, "Listen": 25, "Locksmith" : 1, \
                  "Martial Arts": 1, }
    CharCombatSkills = {}

    def __init__(self):
        return super(CthulhuCharacter, self).__init__(*args, **kwargs)

    def EDURoll(self):
        result = 0
        for i in range(3):
            dicethrow = random.randint(1, 6)
            result += dicethrow
        result += 3
        return result

    def PercentRoll(self)_
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
