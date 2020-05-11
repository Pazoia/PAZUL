import random
from collections import OrderedDict
from pazul.exceptions import EmptyTileCollectionError

class TileCollection:
    def __init__(self):
        self.tiles = OrderedDict()
        self.size = 0

    def add_tile(self, color):
        self.tiles[color] = self.tiles.get(color, 0) + 1
        self.size += 1

    def add_tiles(self, color, quantity):
        self.tiles[color] = self.tiles.get(color, 0) + quantity
        self.size += quantity

    def take_all_of(self, color):
        tiles_to_take = self.tiles.get(color, 0)
        self.tiles[color] = 0
        self.size = self.size - tiles_to_take
        return tiles_to_take

    def take_all(self):
        tiles_to_take = self.tiles
        self.tiles = OrderedDict()
        self.size = 0
        return tiles_to_take

    def take_random(self):
        if self.size == 0:
            raise EmptyTileCollectionError()

        chosen_number = random.randint(1, self.size)

        counter = 0
        for color in self.tiles:
            counter = counter + self.tiles[color]
            if chosen_number <= counter:
                self.tiles[color] = self.tiles[color] - 1
                self.size -= 1
                return color
