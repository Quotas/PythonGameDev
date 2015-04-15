from characters.PlayerClass import *


class Game(object):

  
  def __init__(self, player, encounter):
    
    self.player = player
    self.active = True;
    self.encounter = encounter
    self.needPlayerInput = False;
    
  
  def update(self):
    
    self.player.update()

    if self.encounter.Active:
      print "Careful traveler, " + self.encounter.descrip
      self.needPlayerInput = True
      if self.player.hasresponded:
        for r in self.encounter.posResponse:
          if r == self.encounter.pResponse:
            self.encounter.handleEncounter()
            self.encounter.active = False
            self.player.hasresponded = False
      
  def roll(self):
    return randrange(0, 20)
