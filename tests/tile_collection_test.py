from src.tile_collection import TileCollection

def test_add_one_blue_tile():
    tileCollection = TileCollection()
    tileCollection.add_tile("blue")
    assert tileCollection.bag["blue"] == 1

def test_add_many_tile():
    tileCollection = TileCollection()
    for i in range(20):
        tileCollection.add_tile("blue")
    assert tileCollection.bag["blue"] == 20

def test_add_one_red_tile():
    tileCollection = TileCollection()
    tileCollection.add_tile("red")
    assert tileCollection.bag["red"] == 1
