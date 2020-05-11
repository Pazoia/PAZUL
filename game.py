from pazul.tile_collection import TileCollection

class Game():
    def __init__(self):
        self.STARTING_TILES = 20

    def new_game(self):
        self.bag = TileCollection()
        self.bag.add_tiles("blue", self.STARTING_TILES)
        self.bag.add_tiles("red", self.STARTING_TILES)
        self.bag.add_tiles("orange", self.STARTING_TILES)
        self.bag.add_tiles("purple", self.STARTING_TILES)
        self.bag.add_tiles("pink", self.STARTING_TILES)

        print(self.bag.__dict__)

        self.factory = TileCollection()
        for i in range(4):
            self.factory.add_tile(self.bag.take_random())
        
        print(self.factory.__dict__)

        print(self.bag.__dict__)

game = Game()
game.new_game()

