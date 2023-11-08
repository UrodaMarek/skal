import ascii_art

class Biom:
    def __init__(self, name, delay, char):
        self.name = name
        self.delay = delay
        self.char = char

class Structures:
    def __init__(self, name, delay, char):
        self.name = name
        self.delay = delay
        self.char = char

def gen_world():
    world = []
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
                        world[i].append(Biom("miasto", 0, 'O'))
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