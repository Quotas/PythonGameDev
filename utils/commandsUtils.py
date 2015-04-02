from commands import *

commands = {

	'help' : help ,
	'exit' : exit,
	'eat'  : eat,
	'encounter' : encounter
}


def runCMD(command, args, player):
	commands[command](player, args)

def getCommand(command):
	pass

def setCommand(command, args):
	commands.update({command : args})


def isValidCMD(command):
	if command in commands:
		return True
	return False
