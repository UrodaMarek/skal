from time import sleep
from interface import say, prefix, clear, command_line
from ascii_art import odin_face, village_6_map
from world import gen_village, print_world
from entity.human import Human, Hero
from dialogs.mother import wake_up

def prologue(save_data):
    say("""
Słów mych słuchajcie, potomkowie święci,
Wyżsi i niżsi Heimdalla synowie,
Każesz mi mówić, Ojcze Wszechpotężny
O dawnych dziejach, jak sięgnąć pamięcią

Pomnę olbrzymów przed wieki poczętych
Co piastunami byli moimi
I pomnę dziewięć światów i dziewięć
Świętego drzewa korzeni w głąb ziemi.""")
    sleep(0.5)
    clear()
    for i in range(4):
        print(odin_face)
        clear()
        sleep(0.5)
    wake_up("Matka", "Nói")
    world = gen_village(village_6_map)
    hero = Hero.create_pre_hero({'x': 40,'y': 7})
    hero.pre_object = world[hero.position['y']][hero.position['x']]
    world[hero.position['y']][hero.position['x']] = hero
    pre_world_map = None
    while 1 < 2:
        print_world(world)
        returned = command_line(hero, world, pre_world_map, "", save_data)
        clear()
        if type(returned) == dict:
            return (returned, False)
        elif type(returned) == tuple:
            hero = returned[0]
            world = returned[1]
            pre_world_map = returned[2]
