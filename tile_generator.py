import random
from tile import Tile
from game_input import GameInput
from player import player

class TileGenerator:
    def __init__(self):
        self.tile_names = ["House", "River", "Forest", "Hill", "Barn", "Castle",
                           "Bridge", "Swamp", "Building", "Garden", "Factory",
                           "Forest", "Forest", "Forest", "Forest", "Road",
                           "Road", "Road", "Road", "Forest", "River",
                           "Forest", "Road", "Plain", "Plain", "Plain"]

    def generate_first(self):
        name = random.choice(self.tile_names)

        tile = Tile(0, 0, name)

        tile_str = str(tile.x) + " " +  str(tile.y) + " " + str(tile.name)

        world = open("world.txt", "w")
        world.write(tile_str + "\n")
        world.close()

    def generate_all(self):
        for x in range(1, 351):
            for y in range(1, 351):
                name = random.choice(self.tile_names)

                new_tile = Tile(x, y, name)

                tile_str = str(new_tile.x) + " " +  str(new_tile.y) + " " + str(new_tile.name)

                world = open("world.txt", "a")
                world.write(tile_str + "\n")
                world.close()

        print "[DONE]"

    def load_world(self):
        with open("world.txt") as f:
               tiles = f.readlines()
               for tile in tiles:
                   tile.split()
