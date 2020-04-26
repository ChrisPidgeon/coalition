#author Chris Pidgeon
#Defines all map tiles and how they interact.

import items, enemies 

class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro(self):
        raise NotImplementedError

    def modify(self, player):
        raise NotImplementedError

class IntroTile(MapTile):
    def intro(self):
        return """
        
        """