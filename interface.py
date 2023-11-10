from sys import stdout
from time import sleep
from os import system
from entity.human import Hero
import ascii_art
from world import gen_village, gen_world, find_hero

clear = lambda: system('clear')

def say(words):
    for char in words:
        stdout.write(char)
        stdout.flush()
        sleep(0.06)

def prefix(title):
    input0 = input("███:[ " + title + " ]:███⮞ ")
    return input0

def command_line(hero, world_map, pre_world_map, info, save_data):
    input0 = prefix(hero.name+' '+hero.surname)
    input0 = input0.strip()
    command, flag = input0.split(' ')
    wall_chars = ('.','┋','┅','═','║','╝','╔','╗','╚','&','%')
    match command:
        case 'go':
            match flag:
                case 'north':
                    if world_map[hero.position['y'] - 1][hero.position['x']].char == 'O':
                        match gen_village(world_map[hero.position['y'] - 1][hero.position['x']].village_number):
                            case 0:
                                str_map = ascii_art.village_0_map
                            case 1:
                                str_map = ascii_art.village_1_map
                            case 2:
                                str_map = ascii_art.village_2_map
                            case 3:
                                str_map = ascii_art.village_3_map
                            case 4:
                                str_map = ascii_art.village_4_map
                            case 5:
                                str_map = ascii_art.village_5_map
                            case 6:
                                str_map = ascii_art.village_6_map
                        pre_world_map = world_map
                        world_map = gen_village(str_map)
                        hero.change_position({'x': int(len(world_map[-1]/2)), 'y': -1})
                        hero.pre_object = world_map[hero.position['y']][hero.position['x']]
                        world_map[hero.position['y']][hero.position['x']] = hero
                        return (hero, world_map, pre_world_map)

                    elif world_map[hero.position['y'] - 1][hero.position['x']].char == 'Æ':
                        world_map = pre_world_map
                        hero.pre_object = find_hero(pre_world_map).pre_object
                        hero.change_position(find_hero(pre_world_map).position)
                        return (hero, world_map, None)

                    else:
                        if ((hero.position['y'] - 1) < 0):
                            return (hero, world_map, None)
                        for wall_char in wall_chars:
                            if (world_map[hero.position['y'] - 1][hero.position['x']].char == wall_char):
                                return (hero, world_map, None)
                        world_map[hero.position['y']][hero.position['x']] = hero.pre_object
                        hero.pre_object = world_map[hero.position['y'] - 1][hero.position['x']]
                        hero.change_position({'x': 0, 'y': -1})
                        world_map[hero.position['y']][hero.position['x']] = hero
                        return (hero, world_map, None)

                case 'south':
                    if world_map[hero.position['y'] + 1][hero.position['x']].char == 'O':
                        match gen_village(world_map[hero.position['y'] + 1][hero.position['x']].village_number):
                            case 0:
                                str_map = ascii_art.village_0_map
                            case 1:
                                str_map = ascii_art.village_1_map
                            case 2:
                                str_map = ascii_art.village_2_map
                            case 3:
                                str_map = ascii_art.village_3_map
                            case 4:
                                str_map = ascii_art.village_4_map
                            case 5:
                                str_map = ascii_art.village_5_map
                            case 6:
                                str_map = ascii_art.village_6_map
                        pre_world_map = world_map
                        world_map = gen_village(str_map)
                        hero.change_position({'x': int(len(world_map[-1]/2)), 'y': -1})
                        hero.pre_object = world_map[hero.position['y']][hero.position['x']]
                        world_map[hero.position['y']][hero.position['x']] = hero
                        return (hero, world_map, pre_world_map)

                    elif world_map[hero.position['y'] + 1][hero.position['x']].char == 'Æ':
                        world_map = pre_world_map
                        hero.pre_object = find_hero(pre_world_map).pre_object
                        hero.change_position(find_hero(pre_world_map).position)
                        return (hero, world_map, None)

                    else:
                        if ((hero.position['y'] + 1) > len(world_map)):
                            return (hero, world_map, None)
                        for wall_char in wall_chars:
                            if (world_map[hero.position['y'] + 1][hero.position['x']].char == wall_char):
                                return (hero, world_map, None)
                        world_map[hero.position['y']][hero.position['x']] = hero.pre_object
                        hero.pre_object = world_map[hero.position['y'] + 1][hero.position['x']]
                        hero.change_position({'x': 0, 'y': 1})
                        world_map[hero.position['y']][hero.position['x']] = hero
                        return (hero, world_map, None)

                
                case 'east':
                    if world_map[hero.position['y']][hero.position['x'] + 1].char == 'O':
                        match gen_village(world_map[hero.position['y']][hero.position['x'] + 1].village_number):
                            case 0:
                                str_map = ascii_art.village_0_map
                            case 1:
                                str_map = ascii_art.village_1_map
                            case 2:
                                str_map = ascii_art.village_2_map
                            case 3:
                                str_map = ascii_art.village_3_map
                            case 4:
                                str_map = ascii_art.village_4_map
                            case 5:
                                str_map = ascii_art.village_5_map
                            case 6:
                                str_map = ascii_art.village_6_map
                        pre_world_map = world_map
                        world_map = gen_village(str_map)
                        hero.change_position({'x': int(len(world_map[-1]/2)), 'y': -1})
                        hero.pre_object = world_map[hero.position['y']][hero.position['x']]
                        world_map[hero.position['y']][hero.position['x']] = hero
                        return (hero, world_map, pre_world_map)

                    elif world_map[hero.position['y']][hero.position['x'] + 1].char == 'Æ':
                        world_map = pre_world_map
                        hero.pre_object = find_hero(pre_world_map).pre_object
                        hero.change_position(find_hero(pre_world_map).position)
                        return (hero, world_map, None)

                    else:
                        if ((hero.position['x'] + 1) > len(world_map[0])):
                            return (hero, world_map, None)
                        for wall_char in wall_chars:
                            if (world_map[hero.position['y']][hero.position['x'] + 1].char == wall_char):
                                return (hero, world_map, None)
                        world_map[hero.position['y']][hero.position['x']] = hero.pre_object
                        hero.pre_object = world_map[hero.position['y']][hero.position['x'] + 1]
                        hero.change_position({'x': 1, 'y': 0})
                        world_map[hero.position['y']][hero.position['x']] = hero
                        return (hero, world_map, None)

                case 'west':
                    if world_map[hero.position['y']][hero.position['x'] - 1].char == 'O':
                        match gen_village(world_map[hero.position['y']][hero.position['x'] - 1].village_number):
                            case 0:
                                str_map = ascii_art.village_0_map
                            case 1:
                                str_map = ascii_art.village_1_map
                            case 2:
                                str_map = ascii_art.village_2_map
                            case 3:
                                str_map = ascii_art.village_3_map
                            case 4:
                                str_map = ascii_art.village_4_map
                            case 5:
                                str_map = ascii_art.village_5_map
                            case 6:
                                str_map = ascii_art.village_6_map
                        pre_world_map = world_map
                        world_map = gen_village(str_map)
                        hero.change_position({'x': int(len(world_map[-1]/2)), 'y': -1})
                        hero.pre_object = world_map[hero.position['y']][hero.position['x']]
                        world_map[hero.position['y']][hero.position['x']] = hero
                        return (hero, world_map, pre_world_map)

                    elif world_map[hero.position['y']][hero.position['x'] - 1].char == 'Æ':
                        world_map = pre_world_map
                        hero.pre_object = find_hero(pre_world_map).pre_object
                        hero.change_position(find_hero(pre_world_map).position)
                        return (hero, world_map, None)

                    else:
                        if ((hero.position['x'] - 1) < 0):
                            return (hero, world_map, None)
                        for wall_char in wall_chars:
                            if (world_map[hero.position['y']][hero.position['x'] - 1].char == wall_char):
                                return (hero, world_map, None)
                        world_map[hero.position['y']][hero.position['x']] = hero.pre_object
                        hero.pre_object = world_map[hero.position['y']][hero.position['x'] + 1]
                        hero.change_position({'x': -1, 'y': 0})
                        world_map[hero.position['y']][hero.position['x']] = hero
                        return (hero, world_map, None)
                case _:
                    pass
        case 'menu':
            menu(info, True, save_data)
        case _:
            pass