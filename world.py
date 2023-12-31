import ascii_art

class Biom:
    def __init__(self, name, delay, char):
        self.name = name
        self.delay = delay
        self.char = char

class Village(Biom):
    def __init__(self, name, delay, char, village_number):
        self.village_number = village_number
        super().__init__(name, delay, char)
class Structures:
    def __init__(self, name, delay, char):
        self.name = name
        self.delay = delay
        self.char = char

def gen_world():
    world = []
    increment_of_houses = 0
    village_number = 1
    for i in range(0, 220):
        world.append([])
        for j in range(0, 272):
            map_char = ascii_art.gotland_map[i*273+j]
            if not map_char == '\n':
                match map_char:
                    case '.':
                        world[i].append(Biom("morze", 0, '.'))
                    case '$':
                        world[i].append(Biom("równina", 1, '$'))
                    case 'Ñ':
                        world[i].append(Biom("las", 2, 'Ñ'))
                    case '⁕':
                        world[i].append(Biom("plarza", 3, '⁕'))
                    case 'O':
                        world[i].append(Village("miasto", 0, 'O', village_number))
                        increment_of_houses += 1
                        match increment_of_houses:
                            case 2:
                                village_number = 6
                            case 3:
                                village_number = 5
                            case 6:
                                village_number = 4
                            case 19:
                                village_number = 3
                            case 25:
                                village_number = 2
                            case 29:
                                village_number = 1
                            case 31:
                                village_number = 0
    return world

def gen_village(str_map):
    village = []
    len_cols = str_map.index('\n')+1
    len_row = int(len(str_map)/len_cols)
    
    for i in range(0, len_row):
        village.append([])
        for j in range(0, len_cols):
            map_char = str_map[i*len_cols+j]
            if not map_char == '\n':
                match map_char:
                    case 'Æ':
                        village[i].append(Structures("exit", 0, 'Æ'))
                    case '█':
                        village[i].append(Structures("droga", 1, '█'))
                    case '▒':
                        village[i].append(Structures("trawa", 2, '▒'))
                    case '━':
                        village[i].append(Structures("drzwi_0", 1, '━'))
                    case '┃':
                        village[i].append(Structures("drzwi_1", 1, '┃'))
                    case '▓':
                        village[i].append(Structures("dywan", 1, '▓'))
                    case '┋':
                        village[i].append(Structures("płot_0", 0, '┋'))
                    case '┅':
                        village[i].append(Structures("płot_1", 0, '┅'))
                    case '═':
                        village[i].append(Structures("ściana_0", 0, '═'))
                    case '║':
                        village[i].append(Structures("ściana_1", 0, '║'))
                    case '╗':
                        village[i].append(Structures("kąt_ściany_0", 0, '╗'))
                    case '╔':
                        village[i].append(Structures("kąt_ściany_1", 0, '╔'))
                    case '╚':
                        village[i].append(Structures("kąt_ściany_2", 0, '╚'))
                    case '╝':
                        village[i].append(Structures("kąt_ściany_3", 0, '╝'))
    return village

def find_hero(pre_world_map):
    for i in range(0, 220):
        for j in range(0, 272):
            if pre_world_map[i][j].char == '&':
                return pre_world_map[i][j]

def print_world(world):
    for i in range(0, len(world)):
        for j in range(0, len(world[0])):
            print(world[i][j].char, end='')
        print()

def set_people(tuple_people, world_map):
    for human in tuple_people:
        world_map[human.position['y']][human.position['x']] = human
    
    return world_map