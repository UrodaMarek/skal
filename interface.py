from sys import stdout
from time import sleep
from os import system
from entity.human import Hero
import ascii_art
from world import gen_village, gen_world

clear = lambda: system('clear')

def say(words):
    for char in words:
        stdout.write(char)
        stdout.flush()
        sleep(0.06)

def prefix(title):
    input0 = input("███:[ " + title + " ]:███⮞ ")
    return input0

def command_line(hero, world_map, pre_object):
    input0 = prefix(Hero.name+' '+Hero.surname)
    input0 = input0.strip()
    command, flag = input0.split(' ')
    wall_chars = ('.','Æ','┋','┅','═','║','╝','╔','╗','╚','&','%')
    match command:
        case 'go':
            match flag:
                case 'north':

                    for wall_char in wall_chars:
                        if world_map[hero.position['x']][hero.position['y'] - 1].char == 'O':
                            match gen_village(world_map[hero.position['x']][hero.position['y'] - 1].village_number):
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
                            pre_object = world_map[int(str_map.index('\n')/2)][int(len(str_map)/(str_map.index('\n')))-1]
                            hero.change_position({'x': int((len(str_map)/(str_map.index('\n')))/2), 'y': str_map.index('\n')-1})
                            return (hero, world_map, pre_object, pre_world_map)
                        elif world_map[hero.position['x']][hero.position['y'] - 1].char == 'Æ':
                            ????
                        elif not ((world_map[hero.position['x']][hero.position['y'] - 1].char == wall_char) or ((hero.position['y'] - 1) < 0)):
                            world_map[hero.position['x']][hero.position['y']] = pre_object
                            pre_object = world_map[hero.position['x']][hero.position['y'] - 1]
                            hero.change_position({'x': 0, 'y': -1})
                            return (hero, world_map, pre_object, None)