from interface import prefix, clear
import os
from sys import exit
import json
import datetime
from ascii_art import main_logo, commands_logo, save_logo

def main_menu(game_started, info, save_data):
  clear()
  n = 1
  print(main_logo)
  print("                              "+str(n)+". Nowa gra")
  n += 1
  print("                              "+str(n)+". Wczytaj")
  n += 1
  if (game_started == True):
    print("                               "+str(n)+". Zapisz")
    n += 1
  print("                              "+str(n)+". Komendy")
  n += 1
  if (game_started == False):
    print("                               "+str(n)+". Wyjdź")
  if (game_started == True):
    print("                               "+str(n)+". Wróć")
  print()
  choice = prefix("Wpisz numer bez kropki"+info)
  info = ""
  if (choice == '1'):
    return True
  elif (choice == '2'):
    return load()
  elif ((choice == '3') and (game_started == True)):
    return save(game_started, save_data)
  elif (((choice == '3') and (game_started == False)) or ((choice == '4') and (game_started == True))):
    commands()
  elif ((choice == '4') and (game_started == False)):
    sys.exit()
  elif ((choice == '5') and (game_started == True)):
    return 0
  else:
    info = ", błędna wartość"
    return info

def commands():
  clear()
  print(commands_logo)

def  load():
  clear()
  info=""
  while(1 < 2):
    save_file_existence()
    saves_file = open(".saves/saves.save", "r")
    if not os.stat(".saves/saves.save").st_size == 0:
      print(save_logo)
      print(saves_file.read())
      print()
      saves_file.close()
      name = prefix("Podaj nazwe zapisu"+info)
      info = ""
      if name.startswith('.') or not os.path.exists(".saves/"+name+".json"):
        info = ", brak podanej nazwy"
        continue
      save_file = open(".saves/"+name+".json")
      load = save_file.read()
      save_file.close()
      return json.loads(load)
    else:
      saves_file.close()
      info = ", brak zapisu postępów"
      return info

def save(game_started, save_data):
  clear()
  info=""
  while(1 < 2):
    save_file_existence()
    saves_file = open(".saves/saves.save")
    print(save_logo)
    print(saves_file.read())
    print()
    saves_file.close()
    print()
    name = prefix("Podaj nazwe zapisu"+info)
    info = ""
    if name.startswith('.'):
      info =", błędna nazwa"
      continue
    save_file = open(".saves/"+name+".json", "w")
    save_file.write(json.dumps(save_data))
    save_file.close()
    saves_file = open(".saves/saves.save", "a")
    now = datetime.datetime.now()
    saves_file.write("                              "+name+" - "+str(now)+"\n")
    saves_file.close()
    return 1



def save_file_existence():
  if not os.path.exists(".saves/saves.save"):
      os.makedirs(".saves")
      file = open(".saves/saves.save", "x")
      file.close()