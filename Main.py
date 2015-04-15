from characters.PlayerClass import *
from utils.commandsUtils import *
from utils.commands import *
from utils.generalUtils import *
from gen.RandomEncounters import *
from gen.Game import *
from gen.Threading import *
import threading
import time



player = Player("Default", 1)
encounter = RandomEncounter()
game = Game(player, encounter)




def getInput():
	line = raw_input(">> ")
	user_input = line.split()
	user_input.append("EOI")
	return user_input



def main(player, game):
	user_input = []

	while game.active:
		game.update()
		roll = game.roll()
		
		if (roll >= 14):
			game.encounter.getNewEncounter()
		#if (roll < 14):
		#	print "No encounter started"
		if (game.needPlayerInput):
			user_input = getInput()
			if isValidInput(user_input[0]):
				user_input[0] = game.encounter.pResponse
				player.hasresponded = True
 
	#	if isValidCMD(user_input[0]):
	#		runCMD(user_input[0], user_input[1], player)
		

main(player, game)
