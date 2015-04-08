from characters.PlayerClass import *


class Game(object):

  
  def __init__(self, player, encounter):
    
    self.player = player
    self.active = True;
    self.encounter = encounter
    self.timer = 0
  
  
  def update(self):
    
    self.timer += 1
    
    if (self.timer % 50 == 0):
      self.encounter.getNewEncounter()
    self.player.update()
    if self.encounter.Active:
      print "Careful traveler, " + self.encounter.descrip
      for r in self.encounter.posResponse:
        if r == self.encounter.pResponse:
          self.encounter.handleEncounter()
          self.encounter.active = False
      

