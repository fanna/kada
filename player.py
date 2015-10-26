from tile import Tile

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

name = str(raw_input("Enter your name: "))
player = Player(name, 0, 0)
