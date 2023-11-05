class Thing:
    def __init__(self, name, uses, price):
        self.name = name
        self.uses = uses
        self.price = price

    def use(self):
        self.uses -= 1
        if uses == 0:
            self.name = None
            self.price = None

class Potion(Thing):
    uses = 1
    price = None
    def __init__(self, name, mythology, rarity):
        self.mythology = mythology
        self.rarity = rarity
        super().__init__(name, self.uses, self.price)
    
    def use(self):
        super().use()
        return self.mythology

class Weapon(Thing):
    def __init__(self, name, type_weapon, set_name, set_buffs, buffs, rarity, two_hand, magic, delay, uses, armor, damage, price):
        self.buffs = buffs
        self.rarity = rarity
        self.two_hand = two_hand
        self.delay = delay
        self.damage = damage
        self.armor = armor
        self.magic = magic
        self.type_weapon = type_weapon
        self.set_buffs = set_buffs
        self.set_name = set_name
        super().__init__(name, uses, price*uses)
        
    def attack(self):
        super().use()
        return self.damage

    def vaporize(self):
        super().use()
        return self.armor

class Armor(Thing):
    def __init__(self, name, armor, delay, buffs, rarity, price, uses, set_buffs, set_name, type_armor):
        self.buffs = buffs
        self.rarity = rarity
        self.armor = armor
        self.delay = delay
        self.set_buffs = set_buffs
        self.set_name = set_name
        self.type_armor = type_armor
        super().__init__(name, uses, price*uses)
    def use(self):
        super().use()
        return self.armor

class Amulet(Thing):
    uses = 9_999_999_999
    def __init__(self, name, buffs, rarity, price, set_buffs, set_name):
        self.buffs = buffs
        self.rarity = rarity
        self.set_buffs = set_buffs
        self.set_name = set_name
        super().__init__(name, self.uses, price)

class Food(Thing):
    uses = 3
    def __init__(self, name, rarity, health, price):
        self.health = health
        self.rarity = rarity
        super().__init__(name, self.uses, price*self.uses)

    def use():
        super().use()
        return self.health