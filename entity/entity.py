class Entity:
    dead = False
    def __init__(self, name, health, equipment, delay, attack, concentration):
        self.name = name
        self.health = health
        self.equipment = equipment
        self.delay = delay
        self.attack = attack
        self.concentration = concentration
        self.max_health = health
    def dying(self):
        self.dead = True
        return self.equipment

class Equipment:
    def __init__(self, equipped, things, money):
        self.equipped = equipped
        self.things = things
        self.money = money

    def get_buff(self, name_buff):
        buff_value = 0
        is_equipment_set = self.find_set()
        for thing in self.equipped.values():
            if not (thing == None):
                if (is_equipment_set == True):
                    if not (thing.set_buffs == None):
                        for buff in thing.set_buffs.keys():
                            if (name_buff == buff):
                                buff_value += thing.set_buffs[name_buff]
                else:
                    if not (thing.buffs == None):
                        for buff in thing.buffs.keys():
                            if (name_buff == buff):
                                buff_value += thing.buffs[name_buff]
        return buff_value

    def get_armor(self):
        armor_value = 0
        for thing in self.equipped.values():
            if not (thing == None):
                if not (thing.armor == None):
                    armor_value += thing.armor
        return armor_value

    def get_delay(self):
        delay_value = 0
        for thing in self.equipped.values():
            if not (thing == None):
                if not (thing.delay == None):
                    delay_value += thing.delay
        return delay_value
    
    def get_damage(self):
        damage_value = 0
        for thing in self.equipped.values():
            try:
                if not (thing == None):
                    if not (thing.damage == None):
                        damage_value += thing.damage
            except AttributeError:
                pass
        return damage_value

    def find_set(self):
        set_name = None
        for thing in self.equipped.values():
            if not (thing == None):
                if not (thing.set_name == None):
                    if (set_name == None):
                        set_name = thing.set_name
                    elif not (set_name == thing.set_name):
                        return False
                else:
                    return False
            else:
                return False
        return True