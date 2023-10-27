from interface import prefix
import os
from sys import exit


def main_menu(game_started = True, info = ""):
  print("""
                  █▒▒ ▒▒   █▒▒                  █▒▒
                █▒▒    █▒▒ █▒▒                  █▒▒
                  █▒▒       █▒▒  █▒▒    █▒▒      █▒▒
                    █▒▒     █▒▒ █▒▒   █▒▒  █▒▒   █▒▒
                      █▒▒  █▒█▒▒    █▒▒   █▒▒   █▒▒
                █▒▒    █▒▒ █▒▒ █▒▒  █▒▒   █▒▒   █▒▒
                  █▒▒ ▒▒   █▒▒  █▒▒   █▒▒ █▒▒▒ █▒▒▒

                              1. Nowa gra
                              2. Wczytaj
                               3. Zapisz
                              4. Komendy
                               5. Wyjdź
  """);
  choice = prefix("Wpisz numer bez kropki"+info)
  info = ""
  match(choice):
    case '1':
      return 
    case '2':
      return load()
    case '3':
      save(game_started)
    case '4':
      commands()
    case '5':
      sys.exit()
    case _:
      return [False, ", wcześniej podałeś błędną wartość"]

def commands():
  print()

def  load(info = ""):
  while(1 < 2):
    save_file_existence()
    saves_file = open("~/.skal/saves.save", "r")
    if not os.stat("~/.skal/saves.save").st_size == 0:
      for line in saves_file.readlines():
        print(line)
      saves_file.close()
      name = prefix("Podaj nazwe zapisu"+info)
      info = ""
      if name.startswith('.') or not os.path.exists("~/.skal/"+name+".save"):
        info =", wcześniej podałeś błędną wartość"
        continue
      save_file = open("~/.skal/"+name+".save")
      load = save_file.readlines
      save_file.close()
      return load
    else:
      saves_file.close()
      return 0

def save(game_started):
  if game_started == True:
    save_file_existence()

    save = open("~/.skal/saves.save", "a+")

    for line in save.readlines():
      print(line)

    save.close()

  else:
    return [False, ", nie masz nic do zapisania"]



def save_file_existence():
  if not os.path.exists("~/.skal/saves.save"):
      os.makedirs("~/.skal")
      file = open("~/.skal/saves.save", "w+")
      file.close()