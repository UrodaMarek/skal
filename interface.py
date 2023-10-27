from sys import stdout
from time import sleep

def say(words):
    for char in words:
        stdout.write(char)
        stdout.flush()
        sleep(0.05)

def prefix(title):
    input0 = input("███:[ " + title + " ]:███⮞ ")
    return input0