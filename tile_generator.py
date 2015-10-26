import random
from tile import Tile
from game_input import GameInput
from player import player

class TileGenerator:
    def __init__(self):
        self.tile_names = ["House", "Room", "Forest", "Hill"]

    def generate_first(self):
        name = random.choice(self.tile_names)

        tile = Tile(0, 0, name)

        tile_str = str(tile.x) + " " +  str(tile.y) + " " + str(tile.name)

        world = open("world.txt", "w")
        world.write(tile_str + "\n")
        world.close()

    def generate_north(self):
        name = random.choice(self.tile_names)

        new_tile = Tile(player.x, player.y + 1, name)

        tile_str = str(new_tile.x) + " " +  str(new_tile.y) + " " + str(new_tile.name)
        print tile_str

        world = open("world.txt", "a")
        world.write(tile_str + "\n")
        world.close()

    def generate_south(self):
        name = random.choice(self.tile_names)

        new_tile = Tile(player.x, player.y - 1, name)

        tile_str = str(new_tile.x) + " " +  str(new_tile.y) + " " + str(new_tile.name)
        print tile_str

        world = open("world.txt", "a")
        world.write(tile_str + "\n")
        world.close()

    def generate_east(self):
        name = random.choice(self.tile_names)

        new_tile = Tile(player.x + 1, player.y, name)

        tile_str = str(new_tile.x) + " " +  str(new_tile.y) + " " + str(new_tile.name)
        print tile_str

        world = open("world.txt", "a")
        world.write(tile_str + "\n")
        world.close()

    def generate_west(self):
        name = random.choice(self.tile_names)

        new_tile = Tile(player.x - 1, player.y, name)

        tile_str = str(new_tile.x) + " " +  str(new_tile.y) + " " + str(new_tile.name)
        print tile_str

        world = open("world.txt", "a")
        world.write(tile_str + "\n")
        world.close()

#need to implement parser so I can know which tile is generated
    def parse(self):
        with open("world.txt") as f:
               world = f.readlines()
