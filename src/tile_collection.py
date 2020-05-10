import random
from src.exceptions import EmptyTileCollectionError

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
        self.number_of_tiles = self.number_of_tiles - tiles_to_take
        return tiles_to_take

    def take_all(self):
        tiles_to_take = self.tiles
        self.tiles = {}
        self.number_of_tiles = 0
        return tiles_to_take

    def take_random(self):
        if self.number_of_tiles == 0:
            raise EmptyTileCollectionError()

        chosen_number = random.randint(1, self.number_of_tiles)
        # print(f"chosen number: {chosen_number}")

        counter = 0
        for color in self.tiles:
            if self.tiles[color] != 0:
                counter = counter + self.tiles[color]
                # print(f"color: {color}; counter: {counter}")
                if chosen_number <= counter:
                    self.tiles[color] = self.tiles[color] - 1
                    self.number_of_tiles -= 1
                    # print(f"num tile remaining: {self.number_of_tiles}")
                    # print(f"remaining tiles: {self.tiles[color]}")
                    return color

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


# tileCollection = TileCollection()
# # Adding tiles
# tileCollection.add_tiles("blue", 1)
# tileCollection.add_tiles("red", 1)
# tileCollection.add_tiles("orange", 1)
# tileCollection.add_tiles("green", 1)

# # Taking random tiles
# print(f"take random: {tileCollection.take_random()}")
# print(tileCollection.tiles)
# print("- - - - - - - - - - - - -")
# print(f"take random: {tileCollection.take_random()}")
# print(tileCollection.tiles)
# print("- - - - - - - - - - - - -")
# print(f"take random: {tileCollection.take_random()}")
# print(tileCollection.tiles)
# print("- - - - - - - - - - - - -")
# print(f"take random: {tileCollection.take_random()}")
# print(tileCollection.tiles)
# print("- - - - - - - - - - - - -")
# print(f"take random: {tileCollection.take_random()}")
# print(tileCollection.tiles)
# print("- - - - - - - - - - - - -")
