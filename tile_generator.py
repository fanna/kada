import random
from tile import Tile

class TileGenerator:
    def __init__(self):
        print "Generating tile.."

    def generate_first(self):
        tile_names = ["House", "Room", "Forest", "Hill"]
        NAME = random.choice(tile_names)

        tile = Tile(0, 0, NAME)

        tile_str = str(tile.x) + " " +  str(tile.y) + " " + str(tile.name)

        with open('world.txt', 'w') as file_:
            file_.write(tile_str)

    def generate(self):
        tile_names = ["House", "Room", "Forest", "Hill"] #add more options
        NAME = random.choice(tile_names)

# this needs rewriting, I should know where to generate next tile (on what position)
        if player.move == "N":
            new_tile = Tile(player.x, player.y + 1, NAME)
        if player.move == "S":
            new_tile = Tile(player.x, player.y - 1, NAME)
        if player.move == "E":
            new_tile = Tile(player.x + 1, player.y, NAME)
        if player.move == "W":
            new_tile = Tile(player.x - 1, player.y, NAME)

        tile_str = str(new_tile.x) + " " +  str(new_tile.y) + " " + str(new_tile.name)

        with open('world.txt', 'a') as file_:
            file_.write(tile_str)
