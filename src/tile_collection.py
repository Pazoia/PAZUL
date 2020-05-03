class TileCollection:
    def __init__(self):
        self.tiles = {}

    def add_tile(self, color):
        self.tiles[color] = self.tiles.get(color, 0) + 1

    def add_tiles(self, color, quantity):
        self.tiles[color] = self.tiles.get(color, 0) + quantity

    def take_all_of(self, color):
        tiles_to_take = self.tiles.get(color, 0)
        self.tiles[color] = 0
        return tiles_to_take

    def take_all(self):
        tiles_to_take = self.tiles
        self.tiles = {}
        return tiles_to_take