from CharacterClass import *


class Player(Character):
    def __init__(self, name, health):
        Character.__init__(self, name, health)