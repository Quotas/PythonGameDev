from commands import *
import re

commands = {

	'help' : help,
	'exit' : exit,
	'eat'  : eat,
	'stats' : stats
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

def isValidInput(input, game):
  check = re.compile('^[a-zA-Z]+$')
  if game.encounter.encounterActive:
    if check.match(input):
      return True
    else:
      return False
  return False
    