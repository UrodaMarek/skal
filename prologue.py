from interface import clear, command_line, say
from ascii_art import odin_face, village_6_map
from world import gen_village, print_world, set_people
from entity.human import Human, Hero
from dialogs.mother import wake_up
from dialogs.hero import summary
from cut_scenes import start_prologue

def prologue(save_data):
    start_prologue()

    wake_up("Matka", "Nói")

    world = gen_village(village_6_map)
    hero = Hero.create_pre_hero({'x': 40,'y': 7})
    hero.pre_object = world[hero.position['y']][hero.position['x']]
    mother = Human("Mother", "", 1000, 1000, {}, None, None, None, 1000, {'x': 40, 'y': 6}, "female", "mother")
    set_people((mother, hero),world)
    pre_world_map = None
    can_out = False

    while 1 < 2:
        print_world(world)
        returned = command_line(hero, world, pre_world_map, "", save_data, can_out)
        clear()
        if type(returned) == dict:
            return (returned, False)
        elif type(returned) == tuple:
            hero = returned[0]
            world = returned[1]
            pre_world_map = returned[2]
        if hero.position['y'] > 14:
            break
    
    clear()
    world = gen_village(village_0_map)
    hero = Hero.create_hero({'x': int(len(world[-1]/2)),'y': -1})
    hero.pre_object = world[hero.position['y']][hero.position['x']]
    set_people((mother, hero),world)
    pre_world_map = None
    can_out = False
    home_in_fire()
    say("Gotlandia 15 lat po tragedii")
    summary(hero.name)
    while 1 < 2:
        print_world(world)
        returned = command_line(hero, world, pre_world_map, "", save_data, can_out)
        clear()
        if type(returned) == dict:
            return (returned, False)
        elif type(returned) == tuple:
            hero = returned[0]
            world = returned[1]
            pre_world_map = returned[2]





