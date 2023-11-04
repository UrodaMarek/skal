from menu import main_menu
from world import gen_world, gen_village
import util
import test
import ascii_art

def menu(info, game_started, save_data):
    while 1 < 2:
        menu_return = main_menu(info = info, game_started = game_started, save_data = save_data)
        if menu_return == True:
            return default_data
        elif menu_return.startswith(','):
            info = menu_return
        elif type(menu_return) == dict :
            return menu_return
        elif menu_return == 1:
            continue
        elif menu_return == 0:
            break

default_data = {}
info = ""
game_started = False
save_data = {}
data = menu(info, game_started, save_data)
util.clear()
world = gen_world()
village_0 = gen_village(ascii_art.village_0_map)