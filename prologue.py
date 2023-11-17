from time import sleep
from interface import say, prefix, clear, command_line
from ascii_art import odin_face, village_6_map
from world import gen_village, print_world, set_people
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
