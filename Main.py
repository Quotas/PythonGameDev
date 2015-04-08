from characters.PlayerClass import *
from utils.commandsUtils import *
from utils.commands import *
from utils.generalUtils import *
from gen.RandomEncounters import *
from gen.Game import *


player= Player("Default", 1, 1, 1)
encounter= RandomEncounter()
game= Game(player, encounter)

def main(player):

	while game.active:
	  
		game.update()

		line= raw_input(">> ")
		input= line.split()
		input.append("EOI")

		if isValidCMD(input[0]):
			runCMD(input[0], input[1], player)
		if isValidInput(input[0], game):
			input[0] = game.encounter.pResponse
			
		


main(player)

