import sys
from tile_generator import TileGenerator
from game_input import GameInput
from player import player

def main_menu():
    print("""+------------------------------------------------------------+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|X                                                          X|
|X                                                          X|
|X                                                          X|
|X          __                   __                         X|
|X         /\ \                 /\ \                        X|
|X         \ \ \/'\      __     \_\ \     __                X|
|X          \ \ , <    /'__`\   /'_` \  /'__`\              X|
|X           \ \ ''`\ /\ \L\.\_/\ \L\ \/\ \L\.\_            X|
|X            \ \_\ \_\ \__/.\_\ \___,_\ \__/.\_\           X|
|X             \/_/\/_/\/__/\/_/\/__,_ /\/__/\/_/           X|
|X                                                          X|
|X    A procedurally generated exploration text-adventure   X|
|X                                                          X|
|X                 "Vincit qui se vincit"                   X|
|X                                                          X|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
+------------------------------------------------------------+
+------------------------------------------------------------+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XX      __       XXXXXXXXXXXXXXXXXXXXXXXX                 XX|
|XX     /_/\      X                      X (\.   \      ,/)XX|
|XX    / /\ \     X   1. New Universe    X  \(   |\     )/ XX|
|XX   / / /\ \    X   2. Load Universe   X  //\  | \   /'' XX|
|XX  / / /\ \ \   X   3. Multiplayer     X (/ /\_#oo#_/\ \)XX|
|XX / /_/__\ \ \  X   4. Quit            X  \/\  ####  /\/ XX|
|XX/_/______\_\/\ X                      X       `##'      XX|
|XX\_\_________\/ XXXXXXXXXXXXXXXXXXXXXXXX                 XX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
+------------------------------------------------------------+""")


main_menu()

def menu_loop():
    answer = str(raw_input(">"))

    if answer == "1":
        print "Generating Universe..."
        tile = TileGenerator()
        tile.generate_first()

        game_loop()
    elif answer == "2":
        print "Loading Universe..."
    elif answer == "3":
        print "Not yet implemented!"
        menu_loop()
    elif answer == "4":
        sys.exit("Quit")
    else:
        print "Please chose 1, 2, 3, or 4!"
        menu_loop()

def game_loop():
        tile = TileGenerator()

        player_input = str(raw_input(">"))
#inner IFs are about to change -> they are checking if the tile exists or not
        if player_input == "N":
            if world.tile_exists(player.x, player.y):
                print "exist"
            else:
                tile.generate_north()
        elif player_input == "S":
            if world.tile_exists(player.x, player.y):
                print "exist"
            else:
                tile.generate_south()
        elif player_input == "E":
            if world.tile_exists(player.x, player.y):
                print "exist"
            else:
                tile.generate_east()
        elif player_input == "W":
            if world.tile_exists(player.x, player.y):
                print "exist"
            else:
                tile.generate_west()
        else:
            print "............."

        game_input = GameInput(player_input)
        game_input.input_parse(player_input)

        game_loop()

menu_loop()

