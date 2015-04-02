from random import randrange

class RandomEncounter(object):

    def __init__(self, act):
        self.area = ""
        self.night = True
        self.act = act
        self.type = ""
        self.descripID = ""
        self.descrip = ""
        self.responseActive = False

    def getREncounterTypeID(self):
        typeOfEncounter = [['Puzzle_1', '1$'], [ 'Fight_1', '1#'], ['Stealth_1', '1%']]
        #TODO Add more / read from file?
        rBuffer = randrange(0, len(typeOfEncounter))
        self.type = typeOfEncounter[rBuffer][0]
        self.descripID = typeOfEncounter[rBuffer][1]

    def getEncounterDescrip(self):
        with open('L:\Users\Seamus\Desktop\GameDev2.0\gen\encounterdescrip.txt', 'r') as lBuffer:
            for line in lBuffer:
                lineBuffer = line.split('-')
                if lineBuffer[1] == self.descripID + '\n':
                    self.descrip = lineBuffer[0]

    def getNewEncounter(self):
        self.getREncounterTypeID()
        self.getEncounterDescrip()

    def getEncounterResponse(self):
        self.playerResponseActive = True
