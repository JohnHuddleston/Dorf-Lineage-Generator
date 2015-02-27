import random

#dictionaries for names
maleFirst = ["Ar", "Dar", "Ur", "Sur", "Lad", "Saf", "Raf", "Der", "Bo", "Gam"]
maleLast = ["ist", "ust", "all", "rall", "sohn", "tist", "tol", "dol", "far", "var", "mar", "fur", "ril"]

femaleFirst = ["D", "Sir", "Sar", "Laur", "Dahl", "Mish", "Sish", "Sash", "Tam", "Cam", "Da"]
femaleLast = ["a", "ah", "ka", "da", "ta", "is", "isha", "ishta", "ora", "era"] 

familyFirst = ["Iron", "Gold", "Red", "Dark", "Stone", "Anvil", "Hammer"]
familyLast = ["son", "hammer", "forge", "reach", "crown", "kil", "rett", "mort", "sort"] 

#gender-specific classes	
class Male(object):
	name = random.choice(maleFirst) + random.choice(maleLast)
	family = random.choice(familyFirst) + random.choice(familyLast)
	gender = "male"
	age = random.randint(1, 255)

class Female(object):
	name = random.choice(femaleFirst) + random.choice(femaleLast)
	family = random.choice(familyFirst) + random.choice(familyLast)
	gender = "female"
	age = random.randint(1, 255)

