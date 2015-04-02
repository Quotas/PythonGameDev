from gen.RandomEncounters import *

def help(player, args):
	print "test"
	print player.name

def exit(player, args):
	pass

def eat(player, args):
	pass

def encounter(player, args):
	encounter = RandomEncounter(args)
	encounter.getNewEncounter()
	print encounter.descrip

def processResponse(encounter, input):
	if encounter.type == 'Puzzle':
		pass
	elif encounter.type == 'Fight':
		pass
	elif encounter.type == 'Sealth':


	
