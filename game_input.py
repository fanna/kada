import sys
from player import player

class GameInput:
    def __init__(self, answer):
        self.answer = answer

    def input_parse(self, answer):
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
        elif self.answer == "I":
            self.inventory()
        elif self.answer == "HELP":
            print("""- Enter N to go North
            - Enter S to go South
            - Enter E to go East
            - Enter W to go West
            - Enter I to see the inventory
            - Enter Q to quit the game""")
        else:
            print "Enter HELP to see the commands"

    def inventory(self):
        print("""|<><><><><><><><><><><><><><><><><><><><><><><>---------------------------------------+
|                      *                       ||    ,   ,                            |
|   /\~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~/\    ||   /////|                            |
|  (o )                .                ( o)   ||  ///// |                            |
|   \/               .` `.               \/    || |~~~|  |                            |
|   /\             .`     `.             /\    || |===|  |                            |
|  (             .`         `.             )   || | e |  |                            |
|   )          .`      N      `.          (    || | n |  |                            |
|  (         .`        |        `.         )   || | c | /                             |
|   )      .`         )|(         `.      (    || |===|/                              |
|  (     .`         )  |  (         `.     )   || '---'                               |
|   )  .`         )    |    (         `.  (    ||XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|    .`         )      |      (         `.     ||XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|  .`     W---)--------O--------(---E     `.   ||    Backpack:     |      Using:      |
|   `.          )      |      (          .`    ||                  |                  |
|   ) `.          )    |    (          .` (    ||                  |                  |
|  (    `.          )  |  (          .`    )   ||                  |                  |
|   )     `.          )|(          .`     (    ||                  |                  |
|  (        `.         |         .`        )   ||                  |                  |
|   )         `.       S       .`         (    ||                  |                  |
|  (            `.           .`            )   ||                  |                  |
|   \/            `.       .`            \/    ||                  |                  |
|   /\              `.   .`              /\    ||                  |                  |
|  (o )               `.`               ( o)   ||                  |                  |
|   \/~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~\/    ||                  |                  |
|                     ---                      ||                  |                  |
|<><><><><><><><><><><vvv<><><><><><><><><><><>---------------------------------------+""")
