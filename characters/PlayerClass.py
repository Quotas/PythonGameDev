from CharacterClass import *

class Player(Character):

	
	def __init__(self, name, health, str, int):
		Character.__init__(self, name, health)
		self.str = str
		self.int = int