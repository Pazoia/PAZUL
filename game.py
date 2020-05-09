from src.tile_collection import TileCollection

class Game():
    def __init__(self):
        pass

    def new_game(self):
        self.bag = TileCollection()
        self.bag.add_tiles("blue", 20)
        self.bag.add_tiles("red", 20)
        self.bag.add_tiles("orange", 20)
        self.bag.add_tiles("purple", 20)
        self.bag.add_tiles("pink", 20)

        print(self.bag.__dict__)

game = Game()
game.new_game()

