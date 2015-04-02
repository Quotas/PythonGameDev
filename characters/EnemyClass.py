
from CharacterClass import *

class Enemy(Character):

	def __init__(self, name, health, str):
		Character.__init__(self, name, health)
		self.str = str