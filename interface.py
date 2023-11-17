from sys import stdout
from time import sleep
from os import system
from entity.human import Hero
import ascii_art
from world import gen_village, gen_world, find_hero

clear = lambda: system('clear')

def say(words, name=""):
    if not name == "":
        print(":[ " + name + " ]:⮞ ", end='')
    for char in words:
        stdout.write(char)
        stdout.flush()
        sleep(0.06)
    print()

def prefix(title):
    input0 = input("███:[ " + title + " ]:███⮞ ")
    return input0

def go(x, y, hero, wall_chars, world_map, pre_world_map, can_out):
    if (((hero.position['y'] + y) < 0) or ((hero.position['y'] + y) > (len(world_map) - 1)) or ((hero.position['x'] + x) > (len(world_map[0]) - 1)) or ((hero.position['x'] + x) < 0)):
            return (hero, world_map, pre_world_map)

    elif world_map[hero.position['y'] + y][hero.position['x'] + x].char == 'O':
        match gen_village(world_map[hero.position['y'] + y][hero.position['x'] + x].village_number):
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

    elif (world_map[hero.position['y'] + y][hero.position['x'] + x].char == 'Æ') and (can_out == True):
        world_map = pre_world_map
        hero.pre_object = find_hero(pre_world_map).pre_object
        hero.change_position(find_hero(pre_world_map).position)

    else:
        for wall_char in wall_chars:
            if (world_map[hero.position['y'] + y][hero.position['x'] + x].char == wall_char):
                return (hero, world_map, pre_world_map)
        world_map[hero.position['y']][hero.position['x']] = hero.pre_object
        hero.pre_object = world_map[hero.position['y'] + y][hero.position['x'] + x]
        hero.change_position({'x': x, 'y': y})
        world_map[hero.position['y']][hero.position['x']] = hero

    return hero, world_map, pre_world_map


def command_line(hero, world_map, pre_world_map, info, save_data, can_out):
    input0 = prefix(hero.name+' '+hero.surname)
    input0 = input0.strip()
    try:
        command, flag = input0.split(' ')
    except ValueError:
        command = input0
        flag = ""
    if not flag == "":
        try:
            flag, number_of_movement = flag.split('-')
        except ValueError:
            number_of_movement = 1
    wall_chars = ('.','┋','┅','═','║','╝','╔','╗','╚','&','%')
    match command:
        case 'go':
            for i in range(int(number_of_movement)):
                match flag:

                    case 'n':
                        hero, world_map, pre_world_map = go(0, -1, hero, wall_chars, world_map, pre_world_map, can_out)

                    case 'north':
                        hero, world_map, pre_world_map = go(0, -1, hero, wall_chars, world_map, pre_world_map, can_out)

                    case 's':
                        hero, world_map, pre_world_map = go(0, 1, hero, wall_chars, world_map, pre_world_map, can_out)

                    case 'south':
                        hero, world_map, pre_world_map = go(0, 1, hero, wall_chars, world_map, pre_world_map, can_out)

                    case 'e':
                        hero, world_map, pre_world_map = go(1, 0, hero, wall_chars, world_map, pre_world_map, can_out)

                    case 'east':
                        hero, world_map, pre_world_map = go(1, 0, hero, wall_chars, world_map, pre_world_map, can_out)

                    case 'w':
                        hero, world_map, pre_world_map = go(-1, 0, hero, wall_chars, world_map, pre_world_map, can_out)

                    case 'west':
                        hero, world_map, pre_world_map = go(-1, 0, hero, wall_chars, world_map, pre_world_map, can_out)


                    case _:
                        return (hero, world_map, pre_world_map)
            return (hero, world_map, pre_world_map)

        case 'talk':
            clear()
            if (world_map[hero.position['y'] + 1][hero.position['x']].char == '&'):
                world_map[hero.position['y'] + 1][hero.position['x']].talk(hero.name)
                
            elif (world_map[hero.position['y'] - 1][hero.position['x']].char == '&'):
                world_map[hero.position['y'] - 1][hero.position['x']].talk(hero.name)
                
            elif (world_map[hero.position['y']][hero.position['x'] + 1].char == '&'):
                world_map[hero.position['y']][hero.position['x'] + 1].talk(hero.name)
            
            elif (world_map[hero.position['y']][hero.position['x'] - 1].char == '&'):
                world_map[hero.position['y']][hero.position['x'] - 1].talk(hero.name)
                
        case 'menu':
            menu(info, True, save_data)
        case _:
            pass