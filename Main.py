from characters.PlayerClass import *
from utils.commandsUtils import *
from utils.commands import *
from utils.generalUtils import *
from gen.RandomEncounters import *




player = Player("Default", 1, 1, 1)
encounter = RandomEncounter('test')

def main(player):

	while not player.dead:

		line = raw_input(">> ")
		input = line.split()
		input.append("EOI")

		if isValidCMD(input[0]):
			runCMD(input[0], input[1], player)


main(player)
