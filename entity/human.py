from .entity import Entity, Equipment
import things

class Human(Entity):
    char = '&'
    def __init__(self, name, surname, health, armor, equipment, delay, attack, profession, concentration, position, sex):
        self.surname = surname
        self.profession = profession
        self.position = position
        self.sex = sex
        super().__init__(name, health, equipment, delay, attack, concentration)

    @classmethod
    def create_warrior(cls, name, surname, position):
        equipment = Equipment({"helmet": things.Armor("Lniany kaptur", 5, 0, {"concentration": 2}, "Common", 2, 30, {"concentration": 3, "delay": -2}, "Lniany wojownik", "helmet"), "chest": things.Armor("Skórzany napierśnik", 10, 2, {"armor": 2}, "Common", 2, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "chest"), "legs": things.Armor("Skórzane spodnie", 7, 2, {"armor": 2}, "Common", 2, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "legs"), "boots": things.Armor("Skórzane buty", 3, 1, {"armor": 2}, "Common", 1, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "boots"), "l_hand": things.Weapon("Tarcza świerkowa", "tarcza", None, None, None, "Common", False, False, 3, 50, 5, 0, 2), "r_hand": things.Weapon("Toporek stalowy", "toporek", None, None, None, "Common", False, False, 3, 50, 3, 10, 2), "amulet": None}, [], 10)
        health = 15
        armor = equipment.get_buff("armor") + equipment.get_armor()
        attack = 4 + equipment.get_damage()
        delay = 2 + equipment.get_buff("delay") + equipment.get_delay()
        concentration = 4 + equipment.get_buff("concentration")
        profession = "warrior"
        sex = "male"
        return cls(name, surname, health, armor, equipment, delay, attack, profession, concentration, position, sex)

    @classmethod
    def create_warrior_female(cls, name, surname, position):
        equipment = Equipment({"helmet": None, "chest": things.Armor("Skórzany napierśnik", 10, 2, {"armor": 2}, "Common", 2, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "chest"), "legs": things.Armor("Skórzane spodnie", 7, 2, {"armor": 2}, "Common", 2, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "legs"), "boots": things.Armor("Skórzane buty", 3, 1, {"armor": 2}, "Common", 1, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "boots"), "l_hand": things.Weapon("Tarcza świerkowa", "tarcza", None, None, None, "Common", False, False, 3, 50, 5, 0, 2), "r_hand": things.Weapon("Toporek stalowy", "toporek", None, None, None, "Common", False, False, 3, 50, 3, 10, 2), "amulet": None}, [], 10)
        health = 15
        armor = equipment.get_buff("armor") + equipment.get_armor()
        attack = 3 + equipment.get_damage()
        delay = 1 + equipment.get_buff("delay") + equipment.get_delay()
        concentration = 5 + equipment.get_buff("concentration")
        profession = "warrior"
        sex = "female"
        return cls(name, surname, health, armor, equipment, delay, attack, profession, concentration, position, sex)

    @classmethod
    def create_seidrkona(cls, name, surname, position):
        equipment = Equipment({"helmet": None, "chest": things.Armor("Lniana szata", 5, 3, {"magic": 5}, "Common", 2, 50, {"armor": 3, "magic": 2, "reputation": 3}, "Adeptka seidr", "chest"), "r_hand": things.Weapon("Seidrstafir", "stafir", None, None, {"magic": 10}, "Common", True, True, 5, 50, 3, 2, 3)}, [], 20)
        health = 10
        armor = equipment.get_buff("armor") + equipment.get_armor()
        attack = 1 + equipment.get_damage()
        delay = 0 + equipment.get_buff("delay") + equipment.get_delay()
        concentration = 7 + equipment.get_buff("concentration")
        profession = "seidrkóna"
        sex = "female"
        return cls(name, surname, health, armor, equipment, delay, attack, profession, concentration, position, sex)

    @classmethod
    def create_hunter(cls, name, surname, position):
        equipment = Equipment({"helmet": things.Armor("Lniany kaptur", 5, 0, {"concentration": 2}, "Common", 2, 30, {"concentration": 3, "delay": -2}, "Lniany wojownik", "helmet"), "chest": things.Armor("Skórzany napierśnik", 10, 2, {"armor": 2}, "Common", 2, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "chest"), "legs": things.Armor("Skórzane spodnie", 7, 2, {"armor": 2}, "Common", 2, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "legs"), "boots": things.Armor("Skórzane buty", 3, 1, {"armor": 2}, "Common", 1, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "boots"), "r_hand": things.Weapon("Świerkowy łuk", "łuk", None, None, {"delay": -2, "concentration": 3}, "Common", True, False, 5, 50, 3, 2, 3)}, [things.Food("Pieczone mięso", "Common", 5, 2)], 20)
        health = 20
        armor = equipment.get_buff("armor") + equipment.get_armor()
        attack = 3 + equipment.get_damage()
        delay = 1 + equipment.get_buff("delay") + equipment.get_delay()
        concentration = 5 + equipment.get_buff("concentration")
        profession = "łowca"
        sex = "male"
        return cls(name, surname, health, armor, equipment, delay, attack, profession, concentration, position, sex)

class Hero(Human):
    health = 15 
    name = "Nói"
    surname = "Gunnarsson"
    def __init__(self, position):
        equipment = Equipment({"helmet": things.Armor("Skórzany chełm", 5, 1, {"armor": 2}, "Common", 2, 30, {"armor": 3, "concentration": 3, "delay": -3}, "Skórzany wojownik", "helmet"), "chest": things.Armor("Skórzany napierśnik", 10, 2, {"armor": 2}, "Common", 2, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "chest"), "legs": things.Armor("Skórzane spodnie", 7, 2, {"armor": 2}, "Common", 2, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "legs"), "boots": things.Armor("Skórzane buty", 3, 1, {"armor": 2}, "Common", 1, 50, {"armor": 3, "reputation": 2}, "Skórzany wojownik", "boots"), "l_hand": things.Weapon("Tarcza obita skórą", "tarcza", "Skórzany wojownik", {"armor": 4, "delay": -4}, None, "Common", False, False, 3, 50, 5, 0, 2), "r_hand": things.Weapon("Toporek ze skórzaną rękojeścią", "toporek", "Skórzany wojownik", {"damage": 3}, None, "Common", False, False, 3, 50, 3, 10, 2), "amulet": things.Amulet("Skórzany amulet", {"armor": 3}, "Common", 2, {"armor": 3, "reputation": 2}, "Skórzany wojownik")}, [], 0)
        armor = equipment.get_buff("armor") + equipment.get_armor()
        attack = 5 + equipment.get_damage()
        delay = 2 + equipment.get_buff("delay") + equipment.get_delay()
        concentration = 4 + equipment.get_buff("concentration")
        self.reputation = 100 + equipment.get_buff("reputation")
        profession = "warrior"
        sex = "male"
        super().__init__(self.name, self.surname, self.health, armor, equipment, delay, attack, profession, concentration, position, sex)