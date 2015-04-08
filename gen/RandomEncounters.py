from random import randrange
from path.path import *


class RandomEncounter(object):

    def __init__(self):
        self.type = ""
        self.descripID = ""
        self.descrip = ""
        self.Active = False
        self.pResponse = ""
        self.posResponse = []
        self.getNewEncounter()
        
        
    def getRETypeID(self):
        typeOfEncounter = [['Puzzle_1', '1$'], [ 'Fight_1', '1#'], ['Stealth_1', '1%']]
        #TODO Add more / read from file?
        rBuffer = randrange(0, len(typeOfEncounter))
        self.type = typeOfEncounter[rBuffer][0]
        self.descripID = typeOfEncounter[rBuffer][1]

    def getEDescrip(self):
        with open('/home/ubuntu/workspace/pythongame/PythonGame/gen/encounterdescrip.txt', 'r') as lBuffer:
            for line in lBuffer:
                lineBuffer = line.split('-')
                if lineBuffer[1] == self.descripID + '\n':
                    self.descrip = lineBuffer[0]
                    
    
    def getEPR(self):
      with open('/home/ubuntu/workspace/pythongame/PythonGame/gen/encounterdescrip.txt', 'r') as lBuffer:
            for line in lBuffer:
                lineBuffer = line.split('')
                if lineBuffer[len(lineBuffer)] == self.descripID + '\n':
                    for r in lineBuffer:
                        self.posResponse.append(r)
                        self.posResponse.remove(self.descripID)
    

    def getNewEncounter(self):
        self.getRETypeID()
        self.getEDescrip()
        self.encounterActive = True;

