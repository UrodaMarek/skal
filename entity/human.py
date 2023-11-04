from .entity import Entity
from ascii_art import *

class Human(Entity):
    health = 15
    attack = 2
    speed = 3
    char = '&'
    def __init__(self, name, surname, equipment, ascii_art):
        self.surname = surname
        super().__init__(name, self.health, equipment, self.speed, ascii_art, self.attack)

class Warrior(Entity):
    health = 15
    attack = 2
    speed = 3
    char = '&'
    def __init__(self, name, surname, equipment, ascii_art):
        self.surname = surname
        super().__init__(name, self.health, equipment, self.speed, ascii_art, self.attack)