import random
from pazul.exceptions import EmptyTileCollectionError

class TileCollection:
    def __init__(self):
        self.tiles = {}
        self.number_of_tiles = 0

    def add_tile(self, color):
        self.tiles[color] = self.tiles.get(color, 0) + 1
        self.number_of_tiles += 1

    def add_tiles(self, color, quantity):
        self.tiles[color] = self.tiles.get(color, 0) + quantity
        self.number_of_tiles += quantity

    def take_all_of(self, color):
        tiles_to_take = self.tiles.get(color, 0)
        self.tiles[color] = 0
        return tiles_to_take

    def take_all(self):
        tiles_to_take = self.tiles
        self.tiles = {}
        return tiles_to_take

    def take_random(self):
        chosen_number = random.randint(1, self.number_of_tiles)
        return chosen_number
    
    def take_random_2(self):
        all_tiles = []

        for color in self.tiles:
            times_to_append = self.tiles[color]
            for i in range(times_to_append):
                all_tiles.append(color)

        if len(all_tiles) == 0:
            raise EmptyTileCollectionError()

        chosen_color = random.choice(all_tiles)
        self.tiles[chosen_color] = self.tiles[chosen_color] - 1
        return chosen_color


tileCollection = TileCollection()
# Adding tiles
tileCollection.add_tiles("blue", 20)
print(f"tiles: {tileCollection.tiles}")
print(tileCollection.number_of_tiles)
tileCollection.add_tiles("red", 20)
print(f"tiles: {tileCollection.tiles}")
print(tileCollection.number_of_tiles)
tileCollection.add_tiles("orange", 20)
print(f"tiles: {tileCollection.tiles}")
print(tileCollection.number_of_tiles)
tileCollection.add_tiles("green", 20)
print(f"tiles: {tileCollection.tiles}")
print(tileCollection.number_of_tiles)
tileCollection.add_tiles("purple", 20)
print(f"tiles: {tileCollection.tiles}")
print(tileCollection.number_of_tiles)

# Taking random tiles
tileCollection = TileCollection()
print(f"chosen number: {tileCollection.take_random()}")
