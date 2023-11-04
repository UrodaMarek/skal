from .entity import Entity
from ascii_art import wolf, bear, wild_boar, moose

class Wolf(Entity):
    name = "wilk"
    health = 30
    ascii_art = wolf
    attack = 10
    speed = 2
    def __init__(self, equipment):
        self.equipment = equipment
        super().__init__(self.name, self.health, equipment, self.speed, self.ascii_art, self.attack)


class Bear(Entity):
    name = "niedźwiedź"
    health = 100
    ascii_art = bear
    attack = 40
    speed = 5
    def __init__(self, equipment):
        self.equipment = equipment
        super().__init__(self.name, self.health, equipment, self.speed, self.ascii_art, self.attack)


class Moose(Entity):
    name = "łoś"
    health = 75
    ascii_art = moose
    attack = 4
    def __init__(self, equipment):
        self.equipment = equipment
        super().__init__(self.name, self.health, equipment, self.speed, self.ascii_art, self.attack)


class Wild_boar(Entity):
    name = "dzik"
    health = 35
    ascii_art = wild_boar
    attack = 3
    def __init__(self, equipment):
        self.equipment = equipment
        super().__init__(self.name, self.health, equipment, self.speed, self.ascii_art, self.attack)

