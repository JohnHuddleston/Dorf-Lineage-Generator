import random

#dictionaries for names
maleFirst = ["Ar", "Dar", "Ur", "Sur", "Lad", "Saf", "Raf", "Der", "Bo", "Gam", "Bom", "Da", "Dar", "Dan", "Khi", "Khim", "Lo", "Bel", "Rei", "Thr", "Thra", "Yur"]
maleLast = ["ist", "ust", "all", "rall", "sohn", "tist", "tol", "dol", "far", "var", "mar", "fur", "ril", "ghâl", "in", "fin", "fir", "bur", "bir", "gar"]

femaleFirst = ["D", "Sir", "Sar", "Laur", "Dahl", "Mish", "Sish", "Sash", "Tam", "Cam", "Da", "Lo", "Dar", "Dash", "Hish"]
femaleLast = ["a", "ah", "ka", "da", "ta", "is", "isha", "ishta", "ora", "era", "hilda", "theow", "gal"] 

familyFirst = ["Iron", "Gold", "Red", "Dark", "Stone", "Anvil", "Hammer", "Wolf", "Barrel", "Axe", "Ash", "Amber", "Righteous", "Twilight", "White", "Wind", "Holy", "Glander", "Earth", "Emerald", "Lantern", "Cask", "Cavern"]
familyLast = ["son", "hammer", "forge", "reach", "crown", "kil", "rett", "mort", "sort", "flask", "ale", "arm", "belt", "bringer", "sword", "kindler", "bane", "hood", "mace", "mover", "smith", "speaker"] 

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

#function to generate random dwarf names, tallies by gender and shows totals upon finishing output
def makeDorfs(num):
	numMales = 0
	numFemales = 0
	for i in range(1, num+1):
		if (random.randint(0, 100) >= 50):
			strength = str(random.randint(3, 18))
			dexterity = str(random.randint(3, 18))
			constitution = str(random.randint(3, 18))
			intelligence = str(random.randint(3, 18))
			wisdom = str(random.randint(3, 18))
			charisma = str(random.randint(3, 18))
			print "(Male)", random.choice(maleFirst) + random.choice(maleLast), random.choice(familyFirst) + random.choice(familyLast)
			print "STAT BLOCK: \n Strength: %s \n Dexterity: %s \n Constitution: %s \n Intelligence: %s \n Wisdom: %s \n Charisma: %s" %(strength, dexterity, constitution, intelligence, wisdom, charisma)
			print "*" * 15
			numMales = numMales + 1
		else:
			strength = str(random.randint(3, 18))
			dexterity = str(random.randint(3, 18))
			constitution = str(random.randint(3, 18))
			intelligence = str(random.randint(3, 18))
			wisdom = str(random.randint(3, 18))
			charisma = str(random.randint(3, 18))
			print "(Female)", random.choice(femaleFirst) + random.choice(femaleLast), random.choice(familyFirst) + random.choice(familyLast)
			print "STAT BLOCK: \n Strength: %s \n Dexterity: %s \n Constitution: %s \n Intelligence: %s \n Wisdom: %s \n Charisma: %s" %(strength, dexterity, constitution, intelligence, wisdom, charisma)
			print "*" * 15
			numFemales = numFemales + 1
	print "Number of females:", numFemales, ".  Number of males:", numMales


