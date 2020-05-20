import os
from random import randint
clear = lambda: os.system('cls') #on Windows System
MainLoop = True
LoopOn = True


class Player:
	def __init__(self, health = 0, ac = 0):
		self.health = health
		self.ac = ac

	def printPlayerHealth(self):
		print("player health is: " + str(self.health) + " | player AC = " + str(self.ac))

	def playerHit(self):
		print("You have been hit")
		self.health = self.health - 1
		print ("Your health is " + str(self.health))


class createGoblin:
    def __init__(self,health = 0, arrows = 0, inAction = True):
        self.health = health
        self.arrows = arrows
        self.inAction = inAction

    #def __del__(self):
    #	print("object deleted")

    def getData(self):
        print("Health of goblin: "  + str(self.health) + " Number of arrows: "  + str(self.arrows))

    def doesGoblinLaunchArrow(self):
    	if self.arrows > 0:
    		print("goblin launches arrow")
    		self.arrows = self.arrows - 1 
    		return True
    	else:
    		print("Goblin is running away")
    		self.inAction = False
    		return False



def randomNumberofGoblins():
	numberOfGoblins = randint(1, 6)
	return numberOfGoblins

def doesArrowHit(player, goblin):
	roll = randint(1, 20)
	if roll >= player.ac:
		print("arrow hits")
		player.playerHit()
	else:
		print("arrow miss")
	return roll

def playerAttacksGoblin(player, goblin):
	damage = randint(1, 2)
	goblin.health = goblin.health - damage
	return goblin.health


doesPlayerAttack = False
#----Main Loop----#
while MainLoop == True:
	
	clear()
	print("Welcome to 'Goblin Hunter'")
	print("1. Start new game")
	print("2. Quit game")
	startgame = input()

	if startgame == "1":
		LoopOn = True
		clear()
		player = Player(10, 15)
		numberOfGoblins = randomNumberofGoblins()


		Goblinobjs = list()
		for i in range(numberOfGoblins):
			Goblinobjs.append(createGoblin(randint(1, 2), randint(1, 10)))


		while LoopOn == True:
			player.printPlayerHealth()
			numberOfGoblinsInCombat = len(Goblinobjs)
			print("There are " + str(numberOfGoblinsInCombat) + " goblins in combat.")

			if doesPlayerAttack == True:
				print("You attack the Goblin")
				playerAttacksGoblin(player, Goblinobjs[0])
				#next course pf action could be checkHealth() functions and if it returns <= 0 we delete the object from the array.


			for i in Goblinobjs:
				if i.inAction == True:
					didGoblinLaunch = i.doesGoblinLaunchArrow()			
					if didGoblinLaunch == True:
						print(doesArrowHit(player, i))		
				else:
					print("Goblin not in action")
					Goblinobjs.remove(i)

			for i in Goblinobjs:
				i.getData()
			print("\n")
			
			
			if player.health <= 0:
				print("you have been slain") 
				LoopOn = False
			
			
			if numberOfGoblinsInCombat == 0:
				print("you have survived the Goblin assault. You win!")						
				LoopOn = False
				
			
			print("1: Attack the first Goblin")
			print("press enter to continue or 0 to quit")
			continueBool = input()
			clear()


			if continueBool == "1":
				doesPlayerAttack = True
			else:
				doesPlayerAttack = False
			
			if continueBool == "0":
				LoopOn = False

	else:
		print("quitting")
		MainLoop = False

