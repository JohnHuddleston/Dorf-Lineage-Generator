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
	age = random.randint(40, 300)
	family = random.choice(familyFirst) + random.choice(familyLast)

#gender-specific classes	
class Male(Dwarf):
	name = random.choice(maleFirst) + random.choice(maleLast)
	gender = "male"

class Female(Dwarf):
	name = random.choice(femaleFirst) + random.choice(femaleLast)
	gender = "female"

newDwarf = Male()
print "The golems of the new Earth have created a new dwarf named", newDwarf.name, "who is the originator of the", newDwarf.family, "family, and will die when he is", newDwarf.age

