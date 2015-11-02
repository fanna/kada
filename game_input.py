import sys
from player import player
from tile_generator import TileGenerator
from tile_generator import MIN_RANGE
from tile_generator import MAX_RANGE

class GameInput:
    def __init__(self, answer):
        self.answer = answer

    def input_parse(self, answer):
        tile = TileGenerator()
        if self.answer == "N":
            if player.y < MAX_RANGE:
                player.y += 1
            elif player.y >= MAX_RANGE:
                player.y += 0

            current_pos = "End of the world"

            world = tile.load_world()
            search = str(player.x) + str(player.y)
            for sublist in world:
                if sublist[0] == search:
                    current_pos = sublist[1]
                    break

        #debug info
            print player.name + " is in " + current_pos
            print "On your north is " + self.north_of_you()
            print "On your south is " + self.south_of_you()
            print "On your east is " + self.east_of_you()
            print "On your west is " + self.west_of_you()
        elif self.answer == "S":
            if player.y >= MIN_RANGE:
                player.y -= 1
            elif player.y < MIN_RANGE:
                player.y += 0

            current_pos = "End of the world"

            world = tile.load_world()
            search = str(player.x) + str(player.y)
            for sublist in world:
                if sublist[0] == search:
                    current_pos = sublist[1]
                    break
        #debug info
            print player.name + " is in " + current_pos
            print "On your north is " + self.north_of_you()
            print "On your south is " + self.south_of_you()
            print "On your east is " + self.east_of_you()
            print "On your west is " + self.west_of_you()
        elif self.answer == "E":
            if player.x < MAX_RANGE:
                player.x += 1
            elif player.x >= MAX_RANGE:
                player.x += 0

            current_pos = "End of the world"

            world = tile.load_world()
            search = str(player.x) + str(player.y)
            for sublist in world:
                if sublist[0] == search:
                    current_pos = sublist[1]
                    break
        #debug info
            print player.name + " is in " + current_pos
            print "On your north is " + self.north_of_you()
            print "On your south is " + self.south_of_you()
            print "On your east is " + self.east_of_you()
            print "On your west is " + self.west_of_you()
        elif self.answer == "W":
            if player.x >= MIN_RANGE:
                player.x -= 1
            elif player.x < MIN_RANGE:
                player.x += 0

            current_pos = "End of the world"

            world = tile.load_world()
            search = str(player.x) + str(player.y)
            for sublist in world:
                if sublist[0] == search:
                    current_pos = sublist[1]
                    break
        #debug info
            print player.name + " is in " + current_pos
            print "On your north is " + self.north_of_you()
            print "On your south is " + self.south_of_you()
            print "On your east is " + self.east_of_you()
            print "On your west is " + self.west_of_you()
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

    def north_of_you(self):
        tile = TileGenerator()
        world = tile.load_world()
        north_tile = "None"
        search = str(player.x) + str(player.y + 1)
        for sublist in world:
            if sublist[0] == search:
                north_tile = sublist[1]
                break
        return north_tile

    def south_of_you(self):
        tile = TileGenerator()
        world = tile.load_world()
        south_tile= "None"
        search = str(player.x) + str(player.y - 1)
        for sublist in world:
            if sublist[0] == search:
                south_tile = sublist[1]
                break
        return south_tile

    def east_of_you(self):
        tile = TileGenerator()
        world = tile.load_world()
        east_tile = "None"
        search = str(player.x + 1) + str(player.y)
        for sublist in world:
            if sublist[0] == search:
                east_tile = sublist[1]
                break
        return east_tile

    def west_of_you(self):
        tile = TileGenerator()
        world = tile.load_world()
        west_tile = "None"
        search = str(player.x - 1) + str(player.y)
        for sublist in world:
            if sublist[0] == search:
                west_tile = sublist[1]
                break
        return west_tile
