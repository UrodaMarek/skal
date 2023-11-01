from world import ascii_art

class Biom:
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
