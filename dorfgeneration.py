#!/usr/bin/env python

#Despite not wanting credit, clsr from #/g/sicp @ Rizon made this script as elegant as it is now

#This software is released into public domain.
#It is provided "as is", without warranties or conditions of any kind.
#Anyone is free to use, modify, redistribute and do anything with this software.

import random

#arrays for names
maleFirst = ["Ar", "Dar", "Ur", "Sur", "Lad", "Saf", "Raf", "Der", "Bo", "Gam", "Bom", "Da", "Dar", "Dan", "Khi", "Khim", "Lo", "Bel", "Rei", "Thr", "Thra", "Yur"]
maleLast = ["ist", "ust", "all", "rall", "sohn", "tist", "tol", "dol", "far", "var", "mar", "fur", "ril", "ghal", "in", "fin", "fir", "bur", "bir", "gar"]

femaleFirst = ["D", "Sir", "Sar", "Laur", "Dahl", "Mish", "Sish", "Sash", "Tam", "Cam", "Da", "Lo", "Dar", "Dash", "Hish"]
femaleLast = ["a", "ah", "ka", "da", "ta", "is", "isha", "ishta", "ora", "era", "hilda", "theow", "gal"] 

familyFirst = ["Iron", "Gold", "Red", "Dark", "Stone", "Anvil", "Hammer", "Wolf", "Barrel", "Axe", "Ash", "Amber", "Righteous", "Twilight", "White", "Wind", "Holy", "Glander", "Earth", "Emerald", "Lantern", "Cask", "Cavern"]
familyLast = ["son", "hammer", "forge", "reach", "crown", "kil", "rett", "mort", "sort", "flask", "ale", "arm", "belt", "bringer", "sword", "kindler", "bane", "hood", "mace", "mover", "smith", "speaker"] 

#rolls a MdN; e.g. d(4, 6) rolls a 4d6 and returns a list of 4 ints
def d(m, n): 
	return [random.randint(1, n) for i in range(m)] 

#parent class
class Dorf(object): 
	def __init__(self):
		self.family = random.choice(familyFirst) + random.choice(familyLast)
		self.age = 40 + sum(d(5, 6)) # dwarf adulthood age is 40, starting age is that plus 3d6, 5d6 or 7d6 depending on class
		self.name = None
		self.gender = None
		
		self.strength = sum(sorted(d(4, 6))[1:]) # roll 4d6 and discard the lowest
		self.dexterity = sum(sorted(d(4, 6))[1:])
		self.constitution = sum(sorted(d(4, 6))[1:]) + 2
		self.intelligence = sum(sorted(d(4, 6))[1:])
		self.wisdom = sum(sorted(d(4, 6))[1:])
		self.charisma = sum(sorted(d(4, 6))[1:]) - 2
		
	def __str__(self):
		return '\n'.join([
			'(%s) %s %s' % (self.gender, self.name, self.family),
			'strength: %d' % self.strength,
			'dexterity: %d' % self.dexterity,
			'constitution: %d' % self.constitution,
			'intelligence: %d' % self.intelligence,
			'wisdom: %d' % self.wisdom,
			'charisma: %d' % self.charisma,
		]) 

#gender-specific classes	
class Male(Dorf):
	def __init__(self): 
		super(Male, self).__init__() 
		self.name = random.choice(maleFirst) + random.choice(maleLast)
		self.gender = "male" 

class Female(Dorf):
	def __init__(self):
		super(Female, self).__init__()
		self.name = random.choice(femaleFirst) + random.choice(femaleLast)
		self.gender = "female" 
	
#function to generate random dwarf names, tallies by gender and shows totals upon finishing output
def makeDorfs(num):
	numMales = 0
	numFemales = 0
	for i in range(num): 
		if (random.randint(0, 1) == 1): 
			dorf = Male()
			numMales = numMales + 1
		else:
			dorf = Female()
			numFemales = numFemales + 1
		print(dorf)
		print("*" * 15)
	print('Number of females: %d, Number of males: %d' % (numFemales, numMales)) 

#function to concatenate str input to int with a floating point fallback conversion
def str2int(s):
	try:
		ret = int(s)
	except ValueError:
		ret = float(s)
	return ret	

correctInput = "null"

while (correctInput != "E") and (correctInput != "X"):

	input = raw_input('Issue a command (h for help): ')
	correctInput = input.upper()

	if (correctInput == "H"):
		print('[H] for Help' + '\n' + '[C] for Create Dwarves' + '\n' + '[X] or [E] to Exit' + "\n" + "(Do not include brackets.")

	elif (correctInput == "C"):
		numIt = raw_input("How many dwarves would you like to make? ")
		Iter = str2int(numIt)
		makeDorfs(Iter)

	elif (correctInput == "DEBUG"):
		print (" ________________" + "\n"
			   "|                |" + "\n"
			   "|      ---       |" + "\n"
			   "|  Nice Try Tho  |" + "\n"
			   "|      ---       |" + "\n"
			   "|________________|")

	elif (correctInput == "E") or (correctInput == "X"):
		break

	elif (correctInput == "NULL") or (correctInput == "null"):
		continue

	else:
		print ("Sorry, that is not a recognized command.")
