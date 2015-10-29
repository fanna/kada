import sys
from player import player
from tile_generator import TileGenerator

class GameInput:
    def __init__(self, answer):
        self.answer = answer

    def input_parse(self, answer):
        tile = TileGenerator()
        if self.answer == "N":
            player.y += 1

            current_pos = "End of the world"

            world = tile.load_world()
            search = str(player.x) + str(player.y)
            for sublist in world:
                if sublist[0] == search:
                    current_pos = sublist[1]
                    break
        #debug info
            print player.name + " is in " + current_pos
        elif self.answer == "S":
            player.y -= 1

            current_pos = "End of the world"

            world = tile.load_world()
            search = str(player.x) + str(player.y)
            for sublist in world:
                if sublist[0] == search:
                    current_pos = sublist[1]
                    break
        #debug info
            print player.name + " is in " + current_pos
        elif self.answer == "E":
            player.x += 1

            current_pos = "End of the world"

            world = tile.load_world()
            search = str(player.x) + str(player.y)
            for sublist in world:
                if sublist[0] == search:
                    current_pos = sublist[1]
                    break
        #debug info
            print player.name + " is in " + current_pos
        elif self.answer == "W":
            player.x -= 1

            current_pos = "End of the world"

            world = tile.load_world()
            search = str(player.x) + str(player.y)
            for sublist in world:
                if sublist[0] == search:
                    current_pos = sublist[1]
                    break
        #debug info
            print player.name + " is in " + current_pos
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

        answer = str(raw_input("Inventory: "))
