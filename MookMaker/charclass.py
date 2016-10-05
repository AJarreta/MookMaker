import random
import math

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

    ReferenceCombat = sorted(CharCombatSkills)
    ReferenceSkills = sorted(CharSkills)

    def __init__(self, nationalities, female_names, male_names, languages, personalities, arts):
        self.nationalities = nationalities
        self.female_names = female_names
        self.male_names = male_names
        self.languages = languages
        self.arts = arts
        self.personalities = personalities
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
            if dicethrow < minorresult:
                minorresult = dicethrow
        result -= minorresult
        return result

    def StatRollXHigh(self):
        result = 0
        for i in range(2):
            dicethrow = random.randint(1,6)
            result += dicethrow
        result += 6
        return result

    def SetLanguageSkills(self):
        LanguageIndex = random.randint(0, len(languages) - 1)
        CurrentLanguage = "Other Language:", self.languages[LanguageIndex]
        if "Other Language" in self.CharSkills.keys:
            self.CharSkills[CurrentLanguage] = self.CharSkills.pop("Other Language")
        elif CurrentLanguage in self.CharSkills.keys:
            self.CharSkills[CurrentLanguage] = self.CharSkills.pop(CurrentLanguage)
        else:
            self.CharSkills[CurrentLanguage] = 1
        return CurrentLanguage

    def SetArtSkills(self):
        ArtsIndex = random.randint(0, len(arts) - 1)
        CurrentArt = "Art:", self.arts[ArtsIndex]
        if "Art" in self.CharSkills.keys:
            self.CharSkills[CurrentArt] = self.CharSkills.pop("Art")
        elif CurrentArt in self.CharSkills.keys:
            self.CharSkills[CurrentArt] = self.CharSkills.pop(CurrentArt)
        else:
            self.CharSkills[CurrentArt] = 1
        return CurrentArt

    def PrintCharacter(self):
        pass

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

    ClassSkills = ["Library Use", "Accounting", "Credit Rating", "Fast Talk", "Law", "Persuade", \
                   "Other Language: Latin", "Bargain", "Psychology"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()
    
    def StatsGeneration(self):
        self.CharStats["STR"] = super(Lawyer, self).StatRollNormal()
        self.CharStats["CON"] = super(Lawyer, self).StatRollNormal()
        self.CharStats["SIZ"] = super(Lawyer, self).StatRollXHigh()
        self.CharStats["INT"] = super(Lawyer, self).StatRollXHigh()
        self.CharStats["POW"] = super(Lawyer, self).StatRollHigh()
        self.CharStats["DEX"] = super(Lawyer, self).StatRollNormal()
        self.CharStats["APP"] = super(Lawyer, self).StatRollNormal()
        self.CharStats["EDU"] = super(Lawyer, self).EDURoll()
        self.CharStats["SAN"] = self.CharStats["POW"] * 5
        self.ClassSkillPoints = self.CharStats["EDU"] * 20
        self.FreeSkillPoints = self.CharStats["EDU"] * 10
    
    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested
        self.CharSkills["Other Language: Latin"] = self.CharSkills.pop("Other Language")


    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Lawyer, self).PercentRoll
            if BranchRoll < 75:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested
            
    def PersonalGeneration (self):
        pass
        


class Antiquarian(CthulhuCharacter):

    ClassSkills = ["Library Use", "Law", "Navigate", "Other Language", "Other Language", "History", "Art", "Bargain", "Craft"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Antiquarian, self).PercentRoll
            if BranchRoll < 75:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Parapsychologist(CthulhuCharacter):

    ClassSkills = ["Anthropology", "Archaeology", "Library Use", "Occult", "Other Language", "History", "Psychology", \
                   "Psychoanalysis"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Parapsychologist, self).PercentRoll
            if BranchRoll < 66:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Writer(CthulhuCharacter):

    ClassSkills = ["Library Use", "Fast Talk", "Persuade", "Own Language", "Other Language", "History", "Psychology"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        while range(self.ClassSkills) < 9:
            CurrentRandomSkill = self.ReferenceSkills[random.randint(0, (range(self.ReferenceSkills)-1))]
            if CurrentRandomSkill not in self.ClassSkills:
                self.ClassSkills.append(CurrentRandomSkill)
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Writer, self).PercentRoll
            if BranchRoll < 75:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class PrivateInvestigator(CthulhuCharacter):

    ClassSkills = ["Sneak", "Accounting", "Credit Rating", "Fast Talk", "Law", "Conceal", "Listen", "Disguise", \
                   "Spot Hidden", "Handgun"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if CurrentSkill == "Handgun":
                if (self.CharCombatSkills["Handgun"] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills["Handgun"]
                    self.CharCombatSkills["Handgun"] = 85
            else: 
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(PrivateInvestigator, self).PercentRoll
            if BranchRoll < 50:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Journalist(CthulhuCharacter):
    
    ClassSkills = ["Fast Talk", "Persuade", "Bargain", "Other Language", "Own Language", "Sneak", "Listen"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        while range(self.ClassSkills) < 9:
            CurrentRandomSkill = self.ReferenceSkills[random.randint(0, (range(self.ReferenceSkills)-1))]
            if CurrentRandomSkill not in self.ClassSkills:
                self.ClassSkills.append(CurrentRandomSkill)
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Journalist, self).PercentRoll
            if BranchRoll < 66:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Dilettante(CthulhuCharacter):

    ClassSkills = []

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        while range(self.ClassSkills) < 9:
            CurrentRandomSkill = self.ReferenceSkills[random.randint(0, (range(self.ReferenceSkills)-1))]
            if CurrentRandomSkill not in self.ClassSkills:
                self.ClassSkills.append(CurrentRandomSkill)
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                self.CharSkills[CurrentSkill] = 85
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Dilettante, self).PercentRoll
            if BranchRoll < 75:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    self.CharSkills[CurrentSkill] = 85
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    self.CharCombatSkills[CurrentSkill] = 85
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested



class Doctor(CthulhuCharacter):

    ClassSkills = ["Credit Rating", "First Aid", "Medicine", "Other Language", "Pharmacy", "Psychology", "Psychoanalysis", \
                   "Biology", "Chemistry"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested
        self.CharSkills["Other Language: Latin"] = self.CharSkills.pop("Other Language")


    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Doctor, self).PercentRoll
            if BranchRoll < 75:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    self.CharSkills[CurrentSkill] = 85
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class CollegeProfessor(CthulhuCharacter):

    ClassSkills = ["Anthropology", "Archaeology", "Astronomy", "Biology", "Library Use", "Occult", "Persuade", "Geology", \
                   "Other Language", "History", "Chemistry", "Natural History"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested
        if self.CharSkills["Other Language"] > 1:
            self.SetLanguageSkills()

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(CollegeProfessor, self).PercentRoll
            if BranchRoll < 75:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Revolutionary(CthulhuCharacter):

    ClassSkills = ["Library Use", "Hide", "Conceal", "Disguise", "Sneak", "Fast Talk", "Other Language", "Psychology", "Persuade"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Revolutionary, self).PercentRoll
            if BranchRoll < 50:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Farmer(CthulhuCharacter):

    ClassSkills = ["Spot Hidden", "Operate Heavy Machinery", "Natural History", "Listen", "First Aid", "Bargain", "Biology", \
                   "Drive Auto", "Mechanical Repair"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Farmer, self).PercentRoll
            if BranchRoll < 66:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Politician(CthulhuCharacter):

    ClassSkills = ["Accounting", "Credit Rating", "Fast Talk", "Law", "Persuade", "History", "Bargain", "Psychology", "Listen"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Politician, self).PercentRoll
            if BranchRoll < 75:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Athlete(CthulhuCharacter):

    ClassSkills = ["Credit Rating", "Ride", "Dodge", "Throw", "Swim", "Psychology", "Jump", "Climb", "Martial Arts"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Athlete, self).PercentRoll
            if BranchRoll < 50:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Missionary(CthulhuCharacter):

    ClassSkills = ["Art", "Accounting", "Credit Rating", "Fast Talk", "Medicine", "Other Language", "First Aid", "Bargain", \
                   "Anthropology"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Missionary, self).PercentRoll
            if BranchRoll < 66:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Soldier(CthulhuCharacter):

    ClassSkills = ["Conceal", "Drive Auto", "Operate Heavy Machinery", "Spot Hidden", "Sneak", "Mechanical Repair", "Listen", \
                   "First Aid", "Rifle"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Soldier, self).PercentRoll
            if BranchRoll < 50:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Gangster(CthulhuCharacter):

    ClassSkills = ["Handgun", "Drive Auto", "Credit Rating", "Knife", "Fast Talk", "Law", "Spot Hidden", "Listen", "Bargain", \
                   "Locksmith", "Climb"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Gangster, self).PercentRoll
            if BranchRoll < 50:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Police(CthulhuCharacter):

    ClassSkills = ["Handgun", "Drive Auto", "Fast Talk", "Law", "Spot Hidden", "Sneak", "Listen", "Conceal", "Club", "First Aid"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Police, self).PercentRoll
            if BranchRoll < 50:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested

class Drifter(CthulhuCharacter):

    ClassSkills = ["Fast Talk", "Spot Hidden", "Sneak", "Listen", "Conceal", "First Aid", "Bargain", "Climb", "Locksmith"]

    def CharacterGenerator(self):
        self.StatsGeneration()
        self.DerivedStatsGeneration()
        self.ClassSkillsGeneration()
        self.FreeSkillsGeneration()
        self.PersonalGeneration()

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

    def DerivedStatsGeneration(self):
        self.CharDerivedStats["HP"] = int(math.ceil((self.CharStats["CON"] + self.CharStats["SIZ"]) / float(2)))
        self.CharDerivedStats["Idea"] = self.CharStats["INT"] * 5
        self.CharDerivedStats["Luck"] = self.CharStats["POW"] * 5
        self.CharDerivedStats["MP"] = self.CharStats["POW"]
        self.CharDerivedStats["Knowledge"] = self.CharStats["EDU"] * 5
        BonusDamValue = self.CharStats["STR"] + self.CharStats["SIZ"]
        if BonusDamValue >= 2 and BonusDamValue <= 2:
            self.CharDerivedStats["Dam. Bonus"] = '-1d6'
        elif BonusDamValue >= 13 and BonusDamValue <= 16:
            self.CharDerivedStats["Dam. Bonus"] = '-1d4'
        elif BonusDamValue >= 17 and BonusDamValue <= 24:
            self.CharDerivedStats["Dam. Bonus"] = '0'
        elif BonusDamValue >= 25 and BonusDamValue <= 32:
            self.CharDerivedStats["Dam. Bonus"] = '+1d4'
        elif BonusDamValue >= 33 and BonusDamValue <= 36:
            self.CharDerivedStats["Dam. Bonus"] = '+1d6'

    def ClassSkillsGeneration (self):
        self.CharSkills["Dodge"] = self.CharStats["DEX"] * 2
        self.CharSkills["Own Language"] = self.CharStats["EDU"] * 5
        if self.CharSkills["Own Language"] > 85:
            self.CharSkills["Own Language"] = 85
        while self.ClassSkillPoints > 0:
            CurrentSkill = self.ClassSkills[(random.randint(0, len(self.ClassSkills))) - 1]
            PointsInvested = random.randint(10, 85)
            if (self.ClassSkillPoints - PointsInvested) < 0:
                PointsInvested = self.ClassSkillPoints
            if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                PointsInvested = 85 - self.CharSkills[CurrentSkill]
                self.CharSkills[CurrentSkill] = 85
            else:
                self.CharSkills[CurrentSkill] += PointsInvested
            self.ClassSkillPoints -= PointsInvested

    def FreeSkillsGeneration (self):
        while self.FreeSkillPoints > 0:
            BranchRoll = super(Drifter, self).PercentRoll
            if BranchRoll < 66:
                CurrentSkill = self.ReferenceSkills[(random.randint(0, len(self.ReferenceSkills))) - 1]
                if CurrentSkill == "Other Language":
                    CurrentSkill = self.SetLanguageSkills()
                if CurrentSkill == "Art":
                    CurrentSkill = self.SetArtSkills()
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharSkills[CurrentSkill]
                    self.CharSkills[CurrentSkill] = 85
                else:
                    self.CharSkills[CurrentSkill] += PointsInvested
            else:
                CurrentSkill = ReferenceCombat[(random.randint(0, len(self.ReferenceCombat))) - 1]
                PointsInvested = random.randint(10, 85)
                if (self.FreeSkillPoints - PointsInvested) < 0:
                    PointsInvested = self.FreeSkillPoints
                if (self.CharCombatSkills[CurrentSkill] + PointsInvested) > 85:
                    PointsInvested = 85 - self.CharCombatSkills[CurrentSkill]
                    self.CharCombatSkills[CurrentSkill] = 85
                else:
                    self.CharCombatSkills[CurrentSkill] += PointsInvested
            self.FreeSkillPoints -= PointsInvested
