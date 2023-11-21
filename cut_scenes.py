from interface import clear, say, pause
from time import sleep
from ascii_art import odin_face

def start_prologue():
    say("""
Słów mych słuchajcie, potomkowie święci,
Wyżsi i niżsi Heimdalla synowie,
Każesz mi mówić, Ojcze Wszechpotężny
O dawnych dziejach, jak sięgnąć pamięcią

Pomnę olbrzymów przed wieki poczętych
Co piastunami byli moimi
I pomnę dziewięć światów i dziewięć
Świętego drzewa korzeni w głąb ziemi.""")
    pause()
    clear()
    for i in range(4):
        print(odin_face)
        clear()
        sleep(0.5)