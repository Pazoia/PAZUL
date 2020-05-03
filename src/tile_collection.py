class TileCollection:
    def __init__(self):
        self.bag = {}

    def add_tile(self, color):
        self.bag[color] = self.bag.get(color, 0) + 1