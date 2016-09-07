class CthulhuCharacter(object):
    CharPersonal = {"Name": '', "Age": 0, "Profession": '', "Income": '', "Nationality": '', "Gender": '', "Personality": ''}
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
        self.CharSkills = {"Accounting": 10, "Anthropology": 1, "Archaeology": 1, "Art": 5, "Astronomy": 1, \
                  "Bargain": 5, "Biology": 1, "Chemistry": 1, "Climb": 40, "Conceal": 15, "Craft": 5,\
                  "Credit Rating": 15, "Cthulhu Mythos": 0, "Disguise": 1, "Dodge": 0, "Drive Auto": 20,\
                  "Electric Repair": 10, "Fast Talk": 5, "First Aid": 30, "Geology": 1, "Hide": 10, \
                  "History": 20, "Jump": 25, "Law": 5, "Library Use": 25, "Listen": 25, "Locksmith" : 1, \
                  "Martial Arts": 1, "Mechanical Repair": 20, "Medicine": 5, "Natural History": 10, \
                  "Navigate": 10, "Occult": 5, "Operate Heavy Machinery": 1, "Other Language": 1, \
                  "Own Language": 0, "Persuade": 15, "Pharmacy": 1, "Photography": 10, "Physics": 1, \
                  "Pilot": 1, "Psychoanalysis": 1, "Psychology": 5, "Ride": 5, "Sneak": 10, "Spot Hidden": 25, \
                  "Swim": 25, "Throw": 25, "Track": 10}
        self.CharCombatSkills = {"Fist": 50, "Grapple": 25, "Headbutt": 10, "Kick": 25, "Axe": 20, "Club": 25, "Dagger": 25, \
                        "Knife": 25, "Rapier": 20, "Sabre": 15, "Sword": 10, "Handgun": 20, "Machine Gun": 15, \
                        "Rifle": 25, "Shotgun": 30, "SMG": 15}
        self.ClassSkillPoints = 0
        self.FreeSkillPoints = 0

class Lawyer(CthulhuCharacter):

    ClassSkills = []
    
    def StatsGeneration(self):
        self.CharStats["STR"] = super(Lawyer, self).StatRollNormal()
        self.CharStats["CON"] = super(Lawyer, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Lawyer, self).StatRollXHigh()
        self.CharStats["INT"] = super(Lawyer, self).StatRollXHigh()
        self.CharStats["POW"] = super(Lawyer, self).StatRollHigh
        self.CharStats["DEX"] = super(Lawyer, self).StatRollNormal
        self.CharStats["APP"] = super(Lawyer, self).StatRollNormal
        self.CharStats["EDU"] = super(Lawyer, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5
    
    def DerivedStatsGeneration(self):

class Antiquarian(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Antiquarian, self).StatRollNormal
        self.CharStats["CON"] = super(Antiquarian, self).StatRollNormal
        self.CharStats["SIZ"] = super(Antiquarian, self).StatRollXHigh()
        self.CharStats["INT"] = super(Antiquarian, self).StatRollHigh
        self.CharStats["POW"] = super(Antiquarian, self).StatRollXHigh
        self.CharStats["DEX"] = super(Antiquarian, self).StatRollNormal
        self.CharStats["APP"] = super(Antiquarian, self).StatRollNormal
        self.CharStats["EDU"] = super(Antiquarian, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Parapsychologist(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Parapsychologist, self).StatRollNormal
        self.CharStats["CON"] = super(Parapsychologist, self).StatRollNormal
        self.CharStats["SIZ"] = super(Parapsychologist, self).StatRollXHigh()
        self.CharStats["INT"] = super(Parapsychologist, self).StatRollNormal
        self.CharStats["POW"] = super(Parapsychologist, self).StatRollXHigh
        self.CharStats["DEX"] = super(Parapsychologist, self).StatRollNormal
        self.CharStats["APP"] = super(Parapsychologist, self).StatRollHigh
        self.CharStats["EDU"] = super(Parapsychologist, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Writer(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Writer, self).StatRollNormal()
        self.CharStats["CON"] = super(Writer, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Writer, self).StatRollXHigh()
        self.CharStats["INT"] = super(Writer, self).StatRollXHigh()
        self.CharStats["POW"] = super(Writer, self).StatRollNormal()
        self.CharStats["DEX"] = super(Writer, self).StatRollNormal()
        self.CharStats["APP"] = super(Writer, self).StatRollHigh()
        self.CharStats["EDU"] = super(Writer, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class PrivateInvestigator(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(PrivateInvestigator, self).StatRollNormal()
        self.CharStats["CON"] = super(PrivateInvestigator, self).StatRollHigh()
        self.CharStats["SIZ"] = super(PrivateInvestigator, self).StatRollXHigh()
        self.CharStats["INT"] = super(PrivateInvestigator, self).StatRollNormal()
        self.CharStats["POW"] = super(PrivateInvestigator, self).StatRollNormal()
        self.CharStats["DEX"] = super(PrivateInvestigator, self).StatRollXHigh()
        self.CharStats["APP"] = super(PrivateInvestigator, self).StatRollNormal()
        self.CharStats["EDU"] = super(PrivateInvestigator, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Journalist(CthulhuCharacter:

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Journalist, self).StatRollNormal()
        self.CharStats["CON"] = super(Journalist, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Journalist, self).StatRollXHigh()
        self.CharStats["INT"] = super(Journalist, self).StatRollHigh()
        self.CharStats["POW"] = super(Journalist, self).StatRollNormal()
        self.CharStats["DEX"] = super(Journalist, self).StatRollNormal()
        self.CharStats["APP"] = super(Journalist, self).StatRollXHigh()
        self.CharStats["EDU"] = super(Journalist, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Dilettante(CthulhuCharacter):

    def StatsGeneration(self):
        CharStatsWorkCopy = self.CharStats.items()
        XHighStat = 0
        HighStat = 0
        while XHighStat == HigHStat or XHighStat == 2 or HighStat == 2:
            XHighStat = random.randint(0, 6)
            HigHStat = random.randint(0, 6)
        for k, v in CharStatsWorkCopy:
            if k == XHighStat or k == 2:
                self.CharStats[v] = super(Dilettante, self).StatRollXHigh()
            elif k == HighStat:
                self.CharStats[v] = super(Dilettante, self).StatRollHigh()
            else:
                self.CharStats[v] = super(Dilettante, self).StatRollNormal()
        self.CharStats["EDU"] = super(Dilettante, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Doctor(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Doctor, self).StatRollNormal()
        self.CharStats["CON"] = super(Doctor, self).StatRollNormal
        self.CharStats["SIZ"] = super(Doctor, self).StatRollXHigh()
        self.CharStats["INT"] = super(Doctor, self).StatRollHigh()
        self.CharStats["POW"] = super(Doctor, self).StatRollNormal()
        self.CharStats["DEX"] = super(Doctor, self).StatRollXHigh()
        self.CharStats["APP"] = super(Doctor, self).StatRollNormal()
        self.CharStats["EDU"] = super(Doctor, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class CollegeProfessor(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(CollegeProfessor, self).StatRollNormal()
        self.CharStats["CON"] = super(CollegeProfessor, self).StatRollNormal()
        self.CharStats["SIZ"] = super(CollegeProfessor, self).StatRollXHigh()
        self.CharStats["INT"] = super(CollegeProfessor, self).StatRollXHigh()
        self.CharStats["POW"] = super(CollegeProfessor, self).StatRollHigh()
        self.CharStats["DEX"] = super(CollegeProfessor, self).StatRollNormal()
        self.CharStats["APP"] = super(CollegeProfessor, self).StatRollNormal()
        self.CharStats["EDU"] = super(CollegeProfessor, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Revolutionary(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Revolutionary, self).StatRollNormal()
        self.CharStats["CON"] = super(Revolutionary, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Revolutionary, self).StatRollXHigh()
        self.CharStats["INT"] = super(Revolutionary, self).StatRollNormal()
        self.CharStats["POW"] = super(Revolutionary, self).StatRollXHigh()
        self.CharStats["DEX"] = super(Revolutionary, self).StatRollNormal()
        self.CharStats["APP"] = super(Revolutionary, self).StatRollHigh()
        self.CharStats["EDU"] = super(Revolutionary, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Farmer(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Farmer, self).StatRollHigh()
        self.CharStats["CON"] = super(Farmer, self).StatRollXHigh()
        self.CharStats["SIZ"] = super(Farmer, self).StatRollXHigh()
        self.CharStats["INT"] = super(Farmer, self).StatRollNormal()
        self.CharStats["POW"] = super(Farmer, self).StatRollNormal()
        self.CharStats["DEX"] = super(Farmer, self).StatRollNormal()
        self.CharStats["APP"] = super(Farmer, self).StatRollNormal()
        self.CharStats["EDU"] = super(Farmer, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Politician(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Politician, self).StatRollNormal()
        self.CharStats["CON"] = super(Politician, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Politician, self).StatRollXHigh()
        self.CharStats["INT"] = super(Politician, self).StatRollNormal()
        self.CharStats["POW"] = super(Politician, self).StatRollHigh()
        self.CharStats["DEX"] = super(Politician, self).StatRollNormal()
        self.CharStats["APP"] = super(Politician, self).StatRollXHigh()
        self.CharStats["EDU"] = super(Politician, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Athlete(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Athlete, self).StatRollXHigh()
        self.CharStats["CON"] = super(Athlete, self).StatRollHigh()
        self.CharStats["SIZ"] = super(Athlete, self).StatRollXHigh()
        self.CharStats["INT"] = super(Athlete, self).StatRollNormal()
        self.CharStats["POW"] = super(Athlete, self).StatRollNormal()
        self.CharStats["DEX"] = super(Athlete, self).StatRollNormal()
        self.CharStats["APP"] = super(Athlete, self).StatRollNormal()
        self.CharStats["EDU"] = super(Athlete, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Missionary(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Missionary, self).StatRollNormal()
        self.CharStats["CON"] = super(Missionary, self).StatRollHigh()
        self.CharStats["SIZ"] = super(Missionary, self).StatRollXHigh()
        self.CharStats["INT"] = super(Missionary, self).StatRollNormal()
        self.CharStats["POW"] = super(Missionary, self).StatRollXHigh()
        self.CharStats["DEX"] = super(Missionary, self).StatRollNormal()
        self.CharStats["APP"] = super(Missionary, self).StatRollNormal()
        self.CharStats["EDU"] = super(Missionary, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Soldier(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Soldier, self).StatRollXHigh()
        self.CharStats["CON"] = super(Soldier, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Soldier, self).StatRollXHigh()
        self.CharStats["INT"] = super(Soldier, self).StatRollNormal()
        self.CharStats["POW"] = super(Soldier, self).StatRollNormal()
        self.CharStats["DEX"] = super(Soldier, self).StatRollHigh()
        self.CharStats["APP"] = super(Soldier, self).StatRollNormal()
        self.CharStats["EDU"] = super(Soldier, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Gangster(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Gangster, self).StatRollNormal()
        self.CharStats["CON"] = super(Gangster, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Gangster, self).StatRollXHigh()
        self.CharStats["INT"] = super(Gangster, self).StatRollNormal()
        self.CharStats["POW"] = super(Gangster, self).StatRollNormal()
        self.CharStats["DEX"] = super(Gangster, self).StatRollXHigh()
        self.CharStats["APP"] = super(Gangster, self).StatRollHigh()
        self.CharStats["EDU"] = super(Gangster, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Police(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Police, self).StatRollXHigh()
        self.CharStats["CON"] = super(Police, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Police, self).StatRollXHigh()
        self.CharStats["INT"] = super(Police, self).StatRollNormal()
        self.CharStats["POW"] = super(Police, self).StatRollHigh()
        self.CharStats["DEX"] = super(Police, self).StatRollNormal()
        self.CharStats["APP"] = super(Police, self).StatRollNormal()
        self.CharStats["EDU"] = super(Police, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5

class Drifter(CthulhuCharacter):

    def StatsGeneration(self):
        self.CharStats["STR"] = super(Drifter, self).StatRollNormal()
        self.CharStats["CON"] = super(Drifter, self).StatRollXHigh()
        self.CharStats["SIZ"] = super(Drifter, self).StatRollXHigh()
        self.CharStats["INT"] = super(Drifter, self).StatRollNormal()
        self.CharStats["POW"] = super(Drifter, self).StatRollHigh()
        self.CharStats["DEX"] = super(Drifter, self).StatRollNormal()
        self.CharStats["APP"] = super(Drifter, self).StatRollNormal()
        self.CharStats["EDU"] = super(Drifter, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5
