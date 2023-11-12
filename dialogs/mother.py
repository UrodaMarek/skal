from interface import say, prefix, clear

name = "mother"

def wake_up(name, hero_name):
    localization = "Dom"

    say("Wstawaj Nói, już ranek.", name)

    print("""
    1. Już wstaję.
    2. Jeszcze pięć minutek.
    3. *Nie reaguj*
    """)

    while 1 < 2:
        returned = prefix(localization)
        print()
        match returned:
            case '1':
                say("Już wstaję.", hero_name)
                break
            case '2':
                say("Jeszcze 5 minutek.", hero_name)
                say("Wstawaj! Twój brat już wstał.", name)
                break
            case '3':
                break
            case _:
                pass
    say("Znowu masz koszmary?", name)
    clear()

