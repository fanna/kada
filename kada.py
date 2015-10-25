import sys

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
|X                                                          X|
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

def game_loop():
    answer = str(raw_input(">"))

    if answer == "1":
        print "Generating Universe..."
    elif answer == "2":
        print "Loading Universe..."
    elif answer == "3":
        print "Not yet implemented!"
        game_loop()
    elif answer == "4":
        sys.exit("Quit")
    else:
        print "Please chose 1, 2, 3, or 4!"
        game_loop()

game_loop()

