import sys
from player import player

class GameInput:
    def __init__(self, answer):
        self.answer = answer

    def input_parser(self, answer):
        if self.answer == "N":
            player.y += 1
        #debug info
            print "north"
            print player.name + " is on"
            print player.x
            print player.y
        elif self.answer == "S":
            player.y -= 1
        #debug info
            print "south"
            print player.name + " is on"
            print player.x
            print player.y
        elif self.answer == "E":
            player.x += 1
        #debug info
            print "east"
            print player.name + " is on"
            print player.x
            print player.y
        elif self.answer == "W":
            player.x -= 1
        #debug info
            print "west"
            print player.name + " is on"
            print player.x
            print player.y
        elif self.answer == "Q":
            sys.exit("Quit!")
        else:
            print "Enter HELP to see the commands"
