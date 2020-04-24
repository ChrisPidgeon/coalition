#author Chris Pidgeon
#Defines items within the game world.   

# SUPERCLASSES #
class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
    def __init__(self, name, description, value, damage, damage_type):
        self.damage = damage
        self.damage_type = damage_type
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n{}\nValue: {}\nDamage: {}\nDamage Type: {}\n".format(self.name, self.description, self.value, self.damage, self.damage_type)

class Clothing(Item):
    def __init__(self, name, description, value, armour):
        self.armour = armour
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n{}\nValue: {}\nArmour: {}\n".format(self.name, self.description, self.value, self.armour)

# ITEMS #      
class Credits(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name = "Credits", 
        description = "A credit chip displaying {}.".format(str(self.amount)), 
        value = self.amount)

# WEAPONS #
class Handgun(Weapon):
    def __init__(self, name, description, value, damage, damage_type):
        super().__init__(name = "Handgun", 
        description = "One-handed ranged weapon.", 
        value = 10, 
        damage = 10,
        damage_type = "Ranged")
    
# CLOTHING #
class CezarSuit(Clothing):
    def __init__(self, name, description, value, armour):
        super().__init__(name = "Cezar's Suit", 
        description = "Standard issue outfit of an SIA operative.", 
        value = 25, 
        armour = 5)