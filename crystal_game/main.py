"""Adventure game 'Crystal chase'.

A simple game where you need to visit different places to collect 5 crystals to win.

See https://github.com/kretsulaksusha/Crystal_chase.
"""
import datetime
from random import randint
import game


INIT_DES = """
               \33[95mWelcome to the game 'Crystal chase' \U0001F48E\033[00m
                             _______
                            /___|___\\
                            \\   |   /
                             \\  |  / 
                              \\ | /  
                               \\|/

Your task is to find 5 crystals while visiting different places in Lviv.\n
    \033[93mRules:\033[00m
- type north, west, east or south to go to another place
- talk to people
- earn money\n
    \033[93mHints:\033[00m
- commands are highlighted in blue
- current streat is highlighted in green
- warnings are highlighted in yellow
Good lack!"""
print(INIT_DES)

# initialize streats
virmenska = game.LvivStreats("Virmens'ka St")
virmenska.set_description("""\
You are currently on Virmens'ka St.\nLocated in the very heart of modern Lviv, Virmenska (also known as Armenian) street
is full of life yet has retained much of its old time character.
""")

rynok_square = game.LvivStreats('Rynok Square')
rynok_square.set_description("""\
According to archaeological data, the square was planned in the second half of the 13th century, during the reign of
Prince Leo I of Galicia.
""")
ryn_place = game.Place('Lviv Town Hall')
ryn_place.set_description("The tower of Lviv City Hall is 65 meters high and there is magnificent \
panorama of the city's old central part on the tower.")
ryn_place.set_action("Type [\33[34mgo\033[00m] if you want to reach the top of the tower.")
rynok_square.set_place(ryn_place)


kniazia_romana = game.LvivStreats('Kniazia Romana')
kniazia_romana.set_description("""\
You are currently on Kniazia Romana.\nIt stretches from Halytska Square to the intersection of Franka, Levytskyi and Igor Bilozir streets.
""")
rom_place = game.Place("Phone Booth")
rom_place.set_description("According to the legends, this Phone Booth is a very mysterious place \
and nowadays many tourists like to visit it.")
rom_place.set_action("Type [\33[34mgo\033[00m] if you want to go inside.")
kniazia_romana.set_place(rom_place)


pidvalna = game.LvivStreats('Pidvalna St')
pidvalna.set_description('You are currently on Pidvalna St.\nStreet on the border of Halytskyi \
and Lychakivskyi districts of the city of Lviv. It connects the street of Vynnychenka Street \
with Danylo Halytskyi Square.\n')
pid_place = game.Place("Quest room")
pid_place.set_description("This quest room is based on the history of Lviv. Here you can \
learn new things and spend a great time!\nPrice: 50 UAH.")
pid_place.set_action("Type [\33[34mgo\033[00m] to visit this quest room.")
pidvalna.set_place(pid_place)


mykoly_kopernyka = game.LvivStreats('Mykoly Kopernyka St')
mykoly_kopernyka.set_description("You are currently on Mykoly Kopernyka St.\nOne of \
the central streets of Lviv, located in the Halytsky district of the city.\n")
myk_place = game.Place("Bar 'The Last Call'")
myk_place.set_description("Famous bar in Lviv with unique beverages.")
myk_place.set_action("""Type [\33[34mtalk\033[00m] to talk to people in this bar.
Type [\33[34mtake\033[00m] to get a lighter.""")
mykoly_kopernyka.set_place(myk_place)


pototskykh = game.LvivStreats("Palats Hrafiv Potots'kykh")
pototskykh.set_description("You are currently in Palats Hrafiv Potots'kykh.\n\
A bright example of mature historicism architecture, one of the most \
interesting architectural monuments of Lviv.")
pot_place = game.Place("Museum of art")
pot_place.set_description("Modern art and different sculptures made by a \
teenage artist Anya Forger. The most popular one is a crystal covered in ice \
that sparkles and glitters.")
pot_place.set_action("Type [\33[34mmelt\033[00m] if you want to get a crystal.")
pototskykh.set_place(pot_place)


kryva_lypa = game.LvivStreats('Kryva Lypa Passage')
kryva_lypa.set_description("You are currently on Kryva Lypa Passage.\nA street \
in the Halytskyi district of Lviv, connecting Sichovy Striltsiv and Doroshenko streets.")
lypa_place = game.Place("Casino 'City of Dreams'")
lypa_place.set_description("Like gambling? In the 'City of Dreams' you will \
have the best experience of playing games and earning money!")
lypa_place.set_action("Type [\33[34mplay\033[00m] if you want to play and earn money.")
kryva_lypa.set_place(lypa_place)


sichovykh_striltsiv = game.LvivStreats('Sichovykh Striltsiv St')
sichovykh_striltsiv.set_description("You are currently on Sichovykh Striltsiv St.\n\
Street in Halytsky district of Lviv.")
sich_place = game.Place("Lviv Chocolate factory")
sich_place.set_description("Lviv Chocolate factory is the most famous chain of \
shops and cafés with handmade chocolate products in various parts of Ukraine \
creating a 'Lviv unique atmosphere'.\n\
Also you can buy a chocolate here)\n\
Price: 20 UAH.")
sich_place.set_action("Type [\33[34mbuy\033[00m] to buy a chocolate.")
sichovykh_striltsiv.set_place(sich_place)


drahomanova = game.LvivStreats('Drahomanova St')
drahomanova.set_description("You are currently on Drahomanova St.\n\
Street in Halytsky district of the city of Lviv, Citadel area.")
drah_place = game.Place("The Andrei Sheptytskyi National Museum")
drah_place.set_description("The Andrei Sheptytskyi National Museum is \
the world's\nrichest collection of Ukrainian sacred art of the 12th - 18th \
centuries and works of icon painting.\nThis is the place where Connie works.")
drah_place.set_action("Type [\33[34mtalk\033[00m] to talk to Connie.")
drahomanova.set_place(drah_place)


svobody_ave = game.LvivStreats('Svobody Ave')
svobody_ave.set_description("You are currently on Svobody Ave.\n")
svo_place = game.Place("Cafe 'Coffee mine'")
svo_place.set_description("A well-known cafe for their wide range of diverse desserts and coffee. \
Moreover, there is a bibrary where are a plenty of foreign and ukrainian books to read.")
svo_place.set_action("Type [\33[34mgive\033[00m] to give a chocolate to a person.")
svobody_ave.set_place(svo_place)

# linked streats
virmenska.link_streat(rynok_square, 'south')

rynok_square.link_streat(virmenska, 'north')
rynok_square.link_streat(kniazia_romana, 'west')
rynok_square.link_streat(pidvalna, 'south')

kniazia_romana.link_streat(rynok_square, 'east')
kniazia_romana.link_streat(mykoly_kopernyka, 'west')

pidvalna.link_streat(rynok_square, 'north')
pidvalna.link_streat(pototskykh, 'south')

mykoly_kopernyka.link_streat(kniazia_romana, 'east')
mykoly_kopernyka.link_streat(sichovykh_striltsiv, 'south')
mykoly_kopernyka.link_streat(kryva_lypa, 'west')

pototskykh.link_streat(pidvalna, 'north')
pototskykh.link_streat(sichovykh_striltsiv, 'west')

kryva_lypa.link_streat(mykoly_kopernyka, 'east')

sichovykh_striltsiv.link_streat(drahomanova, 'west')
sichovykh_striltsiv.link_streat(svobody_ave, 'south')
sichovykh_striltsiv.link_streat(pototskykh, 'east')
sichovykh_striltsiv.link_streat(mykoly_kopernyka, 'north')

drahomanova.link_streat(sichovykh_striltsiv, 'east')

svobody_ave.link_streat(sichovykh_striltsiv, 'north')

# set people
antonio = game.People('Antonio')
antonio.set_description("Antonio (traver from Italy).")
antonio.set_verbose_description('Here is your path: Mykoly Kopernyka St -> \
Sichovykh Striltsiv St -> Drahomanova St.')
antonio.set_talk("Nice to meet you! I'm a traveler from Italy and this week I was exploring Lviv.\n\
There are so many places to visit here. Once I wanted to reach the top of the Lviv Town Hall but\n\
unfortunately I couldn't get there without a permission. And someone adviced me to meet Connie who's\n\
working at Drahomanova Streat.\nIf you had this kind of problem, now to know how to solve it!")
mykoly_kopernyka.set_people(antonio)

connie = game.People('Connie')
connie.set_description("Hello! I'm Connie.")
connie.set_talk("Nice to meet you! I can help if you want to visit the Lviv Town Hall.")
drahomanova.set_people(connie)


def main():
    """
    Play the game 'Crystal chase'.
    """
    current_streat = virmenska
    permission = False
    backpack = []
    money = 0

    crystals = 0
    start = datetime.datetime.now()

    while crystals != 5:

        print("\n" + "^^^^" * 25)
        current_streat.get_details()

        place = current_streat.place
        if place:
            print(f"\n\033[1mYou are near:\033[00m {place.place}\n\
{place.description}\n{place.action}")

        people = current_streat.people
        if people:
            print('\n\033[1mPeople you can talk to:\033[00m')
            print(people.description)

        print(f"\n\33[1mNumber of crystals:\033[00m {crystals}.")
        print(f"You need {5 - crystals} more to win!")

        print(f"\n\33[1mWallet:\033[00m {money} UAH.")


        command = input("> ")

        if command in current_streat.get_directions():
            # Move in the given direction
            current_streat = current_streat.move(command)
        elif command == "go":
            if current_streat.name == 'Kniazia Romana':
                if current_streat.crystal:
                    code = randint(4, 61)
                    print(f"\nSuddenly, someone called and you decided to answer the \
phone. \U0001F4DE\nThe voice on the phone said 'There is a strongbox on the floor under \
the carpet.\nIf you want to get a CRYSTAL, convert {code} to binary and this will be \
the code to open the strongbox.")
                    user_bin = input('Type in the code:\n> ')
                    if user_bin == bin(code)[2:]:
                        crystals += 1
                        current_streat.crystal = None
                        print("\n\33[7m Congratulations, you have earned one CRYSTAL! \033[00m")
                    else:
                        print("\n\033[93mThis is incorrect. Try again later!\033[00m")
                else:
                    print('\n\033[96mThere is no crystal in here.\033[00m')
            elif current_streat.name == 'Pidvalna St':
                if money >= 50 and current_streat.crystal:
                    money -= 50
                    crystals += 1
                    current_streat.crystal = None
                    print("\n\33[7m Congratulations, while doing test you have earned \
one CRYSTAL! \033[00m")
                elif not current_streat.crystal:
                    print("\n\033[96mThere is no crystal in here.\033[00m")
                else:
                    print("\n\033[93mYou don't have enough money to do this quest. \
Come again later.\033[00m")
            else:
                if current_streat.crystal and permission:
                    crystals += 1
                    current_streat.crystal = None
                    print("\n\33[7m Congratulations, you have reached the top of the tower and \
earned one CRYSTAL! \033[00m")
                elif not permission:
                    print("\n\033[93mGet a permission to visit the Lviv Town Hall.\033[00m")
                else:
                    print("\n\033[96mThere is no crystal in here.\033[00m")
        elif command == "talk":
            # Talk to the people - check whether there is one!
            if people:
                if people.name == 'Antonio':
                    print(f"\n{people.talk}\nIf you don't know where Drahomanova Streat is, \
I can exlain. Do you want me to?")
                    verbose = input("> ").lower().strip()
                    if verbose in ['y', 'yes']:
                        print(f"\n\33[7m {people.verbose} Have a good day!\033[00m ")
                    else:
                        print("\n\33[7m See you later! \033[00m")
                else:
                    print(people.talk + "\nDo you want to get a permission for visiting?\n")
                    user_y_n = input("> ").lower().strip()
                    if user_y_n in ['y', 'yes']:
                        permission = True
                        print("\n\33[7m Now you have a permission! Spent a great time \
exploring! \033[00m")
                    else:
                        print("\n\33[7m See you later! \033[00m")
            else:
                print("\nThere is nobody with this name.")
        elif command == "melt":
            if 'lighter' in backpack and current_streat.crystal:
                current_streat.crystal = None
                crystals += 1
                print("\n\33[7m Congratulations, you have melted the ice and got one \
CRYSTAL! \033[00m")
            elif not current_streat.crystal:
                print("\n\033[96mThere is no crystal in here.\033[00m")
            else:
                print("\n\033[93mYou have no lighter to melt the ice.\033[00m")
        elif command == "play":
            dice = randint(2, 12)
            print("The game is very simple. We have rolled the dice and if the sum is \
more that 7, you will get 10 UAH. Good luck!")
            if dice > 7:
                money += 10
                print("\n\33[7m Congratulations, you have won 10 UAH! \033[00m")
            else:
                print("\n\033[93mThe sum is less than or equal to 7. Try one more time!\033[00m")
        elif command == "buy":
            if money >= 20:
                backpack.append('chocolate')
                money -= 20
                print("\n\33[7m You have bought a unique Lviv chocolate! \033[00m")
            else:
                print("\n\033[93mYou don't have enough money. Come again later.\033[00m")
        elif command == "give":
            if 'chocolate' in backpack and current_streat.crystal:
                print("\nYou were very excited to visit this place and decided to try coffee \
called 'When it's raining' which was one of the best coffees you've ever tried. So you gave \
a chocolate as a tip to the waiter and they gave you a little present too. \U0001f381")
                input("Press 'enter' to open your present!")
                print("\n\33[7m Congratulations, you have got one CRYSTAL! \033[00m")
                current_streat.crystal = None
                crystals += 1
            else:
                print("\n\033[93mYou don't have any chocolate.\033[00m")
        elif command == "take":
            if current_streat.name == 'Mykoly Kopernyka St':
                if 'lighter' not in backpack:
                    print("\n\33[7m You put the lighter in your backpack \033[00m")
                    backpack.append('lighter')
                else:
                    print("\nYou have already lighter in your backpack")
            elif current_streat.name == 'Sichovykh Striltsiv St':
                if 'chocolate' not in backpack:
                    print("\n\33[7m You put chocolate in your backpack \033[00m")
                    backpack.append('chocolate')
                else:
                    print("\nYou have already chocolate in your backpack")
            else:
                print("\n\033[93mThere's nothing here to take!\033[00m")
        else:
            print(f"\n\033[93mThere is no command [{command}].\033[00m")

        # time limit
        if (datetime.datetime.now() - start).seconds > 600:
            print("Time is up. Try again later!")
            break

    if crystals == 5:
        print("\n\33[95mCongratulations!!! You have collected all 5 crystals \
    while visiting Lviv!\033[00m")


if __name__ == "__main__":
    main()
