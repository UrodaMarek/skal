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

def command_line():
    input0 = prefix(Hero.name+' '+Hero.surname)
    input0 = input0.strip()