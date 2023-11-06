from time import sleep
from interface import say, prefix, clear, command_line
from ascii_art import odin_face, village_6_map
from world import gen_village
from entity.human import Human, Hero

def prologue():
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
    dream_world = gen_village(village_6_map)
    pre_hero = Hero.create_pre_hero({'x': 7,'y': 40})
    pre_object = dream_world[pre_hero.position['x']][pre_hero.position['y']]
    command_line(pre_hero, dream_world, pre_object)
