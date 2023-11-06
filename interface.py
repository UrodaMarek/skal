from sys import stdout
from time import sleep
from os import system
from entity.human import Hero

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
                        if not ((world_map[hero.position['x']][hero.position['y'] - 1].char == wall_char) or ((hero.position['y'] - 1) < 0)):
                            world_map[hero.position['x']][hero.position['y']] = pre_object
                            pre_object = world_map[hero.position['x']][hero.position['y'] - 1]
                            hero.change_position({'x': 0, 'y': -1})
                            return (hero, world_map, pre_object)