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
|X    A procedurally generated text-adventure/exploration   X|
|X                                                          X|
|X                 "Vincit qui se vincit"                   X|
|X                                                          X|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
+------------------------------------------------------------+
+------------------------------------------------------------+
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XX      __       XXXXXXXXXXXXXXXXXXXXXXXX                 XX|
|XX     /_/\      X                      X (\.   \      ,/)XX|
|XX    / /\ \     X   1. New world       X  \(   |\     )/ XX|
|XX   / / /\ \    X   2. Load world      X  //\  | \   /'' XX|
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
        print "Generating world..."
        tile = TileGenerator()
        tile.generate_all()

        game_loop()
    elif answer == "2":
        print "Loading world..."
    elif answer == "3":
        print "Not yet implemented!"
        menu_loop()
    elif answer == "4":
        sys.exit("Quit")
    else:
        print "Please chose 1, 2, 3, or 4!"
        menu_loop()

def game_loop():
        player_input = str(raw_input(">"))

        game_input = GameInput(player_input)
        game_input.input_parse(player_input)

        game_loop()

menu_loop()

