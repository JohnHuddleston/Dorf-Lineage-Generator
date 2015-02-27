import random

#dictionaries for names
maleFirst = ["Ar", "Dar", "Ur", "Sur", "Lad", "Saf", "Raf", "Der", "Bo", "Gam"]
maleLast = ["ist", "ust", "all", "rall", "sohn", "tist", "tol", "dol", "far", "var", "mar", "fur", "ril"]

femaleFirst = ["D", "Sir", "Sar", "Laur", "Dahl", "Mish", "Sish", "Sash", "Tam", "Cam", "Da"]
femaleLast = ["a", "ah", "ka", "da", "ta", "is", "isha", "ishta", "ora", "era"] 

familyFirst = ["Iron", "Gold", "Red", "Dark", "Stone", "Anvil", "Hammer"]
familyLast = ["son", "hammer", "forge", "reach", "crown", "kil", "rett", "mort", "sort"] 

#generic dwarf class
class Dwarf(object):
	def __init__(self, family, age):
		self.family = family
		self.age = age
	age = random.uniform(40, 300)
	family = random.choice(familyFirst) + random.choice(familyLast)

#gender-specific classes	
class Male(Dwarf):
	def __init__(self, name):
		self.name = name
	name = random.choice(maleFirst) + random.choice(maleLast)

class Female(Dwarf):
	def __init__(self, name):
		self.name = name
	name = random.choice(femaleFirst) + random.choice(femaleLast)

newDwarf = Male()
print newDwarf.age + newDwarf.name + newDwarf.family

