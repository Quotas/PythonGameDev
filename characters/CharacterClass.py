class Character(object):

	def __init__(self, name, health):


		self.name = name
		self.health = health

		self.dead = False
		self.inventory = []


	def attack(self, other):
		pass

	def update(self):
		if self.health < 0:
			self.dead = True
			self.health = 0

	def loadINV(self):
		with open('L:\Users\Seamus\Desktop\GameDev2.0\characters\inventory.txt') as invBuffer:
			for line in iter(invBuffer.readline, ''):
				lineBuffer = line.split("\n")
				self.inventory.append(lineBuffer[0])

	def pushINV(self):
		with open('L:\Users\Seamus\Desktop\GameDev2.0\characters\inventory.txt', 'w') as invBuffer:
			for item in self.inventory:
				invBuffer.write(item)

	def removeItem(self, item):
		for i in self.inventory:
			if i == item:
				self.inventory.pop([i])
			else:
				pass
				#catch the error if there is no item to remove

	def addItem(self, item):
		self.inventory.append(item)
