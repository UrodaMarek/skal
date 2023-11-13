from interface import say, prefix, clear

name = "mother"

def wake_up(name, hero_name):
    localization = "Dom"
    while 1 < 2:
        say("Wstawaj Nói, już ranek.", name)

        print("""
        1. Już wstaję.
        2. Jeszcze pięć minutek.
        3. *Nie reaguj*
        4. *Wstań*
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
                case '4':
                    say("Dobra wstaje", hero_name)
                    clear()
                    return None
                case _:
                    pass
        say("Znowu masz koszmary?", name)

        print("""
        1. Tak.
        2. Nie.
        """)

        while 1 < 2:
            returned = prefix(localization)
            print()
            match returned:
                case '1':
                    say("Tak. Ciągle ten starzec.", hero_name)
                    say("Powinieneś się udać do jakiegoś kapłana, albo Volvy.", name)
                    say("Te sny są coraz bardziej niepokojące")
                    break
                case '2':
                    say("Nie.", hero_name)
                    say("To dobrze.", name)
                    say("Chociaż tyle, ponieważ wyglądasz jak trup.", name)
                    break
                case _:
                    pass