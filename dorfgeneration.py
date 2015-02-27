import random

#dictionaries for names
maleNameDict = {'first':["Ar", "Dar", "Ur", "Sur", "Lad", "Saf", "Raf", "Der", "Bo", "Gam"], 
'last':["ist", "ust", "all", "rall", "sohn", "tist", "tol", "dol", "far", "var", "mar", "fur", "ril"], }

femaleNameDict = {'first':["D", "Sir", "Sar", "Laur", "Dahl", "Mish", "Sish", "Sash", "Tam", "Cam", "Da"], 
'last':["a", "ah", "ka", "da", "ta", "is", "isha", "ishta", "ora", "era"] }

familyNameDict = {'first':["Iron", "Gold", "Red", "Dark", "Stone", "Anvil", "Hammer"], 
'last':["son", "hammer", "forge", "reach", "crown", "kil", "rett", "mort", "sort"] }

#generic dwarf class
class Dwarf(object):
	def __init__(self, family, age):
		self.family = family
		self.age = age
	age = random.uniform(40, 300)
	family = familyNameDict['first'[random.uniform(0, len(familyNameDict['first']) + 1)]] + familyNameDict[last[random.uniform(0, len(familyNameDict['last']) + 1)]]

#gender-specific classes	
class Male(Dwarf):
	def __init__(self, name):
		self.name = name
	name = maleNameDict['first'[random.uniform(0, len(maleNameDict['first']) + 1)]] + maleNameDict[last[random.uniform(0, len(maleNameDict['last']) + 1)]]

class Female(Dwarf):
	def __init__(self, name):
		self.name = name
	name = femaleNameDict['first'[random.uniform(0, len(femaleNameDict['first']) + 1)]] + femaleNameDict[last[random.uniform(0, len(femaleNameDict['last']) + 1)]]

newDwarf = Male()
print newDwarf.age + newDwarf.name + newDwarf.family

