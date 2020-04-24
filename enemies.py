#author Chris Pidgeon
#Defines enemies within the game world. 

# SUPERCLASSES #
class Enemy():
    def __init__(self, name, health, description, damage, damage_type):
        self.name = name
        self.health = health
        self.description = description
        self.damage = damage
        self.damage_type = damage_type

    def status(self):
        return self.health > 0

# ENEMIES 
class Thug(Enemy):
    def __init__(self, name, health, description, damage, damage_type):
        super().__init__(name = "Thug", 
        health = 50, 
        description = "A typical thug one would think nothing of.", 
        damage = 10, 
        damage_type = "Melee")