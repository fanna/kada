import random
from tile import Tile
from player import player

MIN_RANGE = -5
MAX_RANGE = 5

class TileGenerator:
    def __init__(self):
        self.tile_names = ["House", "River", "Forest", "Hill", "Barn", "Castle",
                           "Bridge", "Swamp", "Building", "Garden", "Factory",
                           "Forest", "Forest", "Forest", "Forest", "Road",
                           "Road", "Road", "Road", "Forest", "River",
                           "Forest", "Road", "Plain", "Plain", "Plain", "Palace"]

    def generate_first(self):
        name = random.choice(self.tile_names)

        new_tile = Tile(0, 0, name)

        tile_str = str(new_tile.x) + str(new_tile.y) + " " + str(new_tile.name)

        world = open("world.txt", "w")
        world.write(tile_str + "\n")
        world.close()

    def generate_all(self):
        for x in range(MIN_RANGE, MAX_RANGE):   #this goes from 1 to 351
            for y in range(MIN_RANGE, MAX_RANGE): #this goes from 1 to 351
                name = random.choice(self.tile_names)

                new_tile = Tile(x, y, name)

                tile_str = str(new_tile.x) + str(new_tile.y) + " " + str(new_tile.name)

                world = open("world.txt", "a")
                world.write(tile_str + "\n")
                world.close()

        print "[DONE]"

    def load_world(self):
        world = []
        with open("world.txt") as f:
               tiles = f.readlines()
               for tile in tiles:
                  parsed_world = tile.split()
                  world.append(parsed_world)

        return world

    def get_names(self):
        names = []
        world = self.load_world()
        for name in range(0, len(world)):
            print world[name][1]

        return names
