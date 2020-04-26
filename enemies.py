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

# ENEMIES #
class Thug(Enemy):
    def __init__(self, name, health, description, damage, damage_type):
        super().__init__(name = "Thug", 
        health = 50, 
        description = "One of the many spacers that have chosen to reject the governments that rule them.", 
        damage = 10, 
        damage_type = "Melee")

class Security_Bot_Melee(Enemy):
    def __init__(self, name, health, description, damage, damage_type):
        super().__init__(name = "Security Bot UC", 
        health = 150, 
        description = "A droid, likely stolen, that has been hacked for darker purposes. This particular bot is equipped with shock batons.", 
        damage = 20, 
        damage_type = "Melee")

class Security_Bot_Ranged(Enemy):
    def __init__(self, name, health, description, damage, damage_type):
        super().__init__(name = "Security Bot FA", 
        health = 125, 
        description = "A droid, likely stolen, that has been hacked for darker purposes. This particular bot is equipped with wrist-mounted lasers.", 
        damage = 15, 
        damage_type = "Ranged")