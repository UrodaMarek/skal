from .entity import Entity

class Wolf(Entity):
    name = "wilk"
    health = 30
    attack = 10
    delay = 2
    concentration = 3
    def __init__(self, equipment):
        self.equipment = equipment
        super().__init__(self.name, self.health, equipment, self.delay, self.attack, self.concentration)


class Bear(Entity):
    name = "niedźwiedź"
    health = 100
    attack = 40
    delay = 5
    def __init__(self, equipment):
        self.equipment = equipment
        super().__init__(self.name, self.health, equipment, self.delay, self.attack, self.concentration)


class Moose(Entity):
    name = "łoś"
    health = 75
    attack = 30
    delay = 6
    def __init__(self, equipment):
        self.equipment = equipment
        super().__init__(self.name, self.health, equipment, self.delay, self.attack, self.concentration)


class Wild_boar(Entity):
    name = "dzik"
    health = 35
    attack = 15
    delay = 1
    def __init__(self, equipment):
        self.equipment = equipment
        super().__init__(self.name, self.health, equipment, self.delay, self.attack, self.concentration)

