class Entity:
    dead = False
    def __init__(self, name, health, equipment, speed, ascii_art, attack):
        self.name = name
        self.health = health
        self.equipment = equipment
        self.ascii_art = ascii_art
        self.speed = speed
    def dying(self):
        self.dead = True
        return self.equipment
