import pytest
import unittest.mock as mock
from src.tile_collection import TileCollection
from src.exceptions import EmptyTileCollectionError

def test_add_one_blue_tile():
    tileCollection = TileCollection()
    tileCollection.add_tile("blue")
    assert tileCollection.tiles["blue"] == 1

def test_add_many_tiles():
    tileCollection = TileCollection()
    tileCollection.add_tiles("blue", 20)
    assert tileCollection.tiles["blue"] == 20

def test_add_one_red_tile():
    tileCollection = TileCollection()
    tileCollection.add_tile("red")
    assert tileCollection.tiles["red"] == 1

def test_take_all_of_return_all_red_tiles():
    tileCollection = TileCollection()
    tileCollection.add_tiles("red", 5)
    assert tileCollection.take_all_of("red") == 5

def test_take_all_of_removes_all_red_tiles():
    tileCollection = TileCollection()
    tileCollection.add_tiles("red", 5)
    tileCollection.take_all_of("red")
    assert tileCollection.tiles["red"] == 0

def test_take_all_of_removes_non_existent_tiles():
    tileCollection = TileCollection()
    assert tileCollection.take_all_of("red") == 0

def test_take_all_return_all_removed_tiles():
    tileCollection = TileCollection()
    tileCollection.add_tiles("red", 5)
    tileCollection.add_tiles("blue", 5)
    taken_tiles = tileCollection.take_all()
    assert taken_tiles == {"red": 5, "blue": 5}

def test_take_all_removes_all_tiles():
    tileCollection = TileCollection()
    tileCollection.add_tiles("red", 5)
    tileCollection.add_tiles("blue", 5)
    tileCollection.take_all()
    assert tileCollection.tiles == {}

def test_take_random_fail_on_empty_collection():
    with pytest.raises(EmptyTileCollectionError):
        TileCollection().take_random()

def choose_blue(values):
    return "blue"

def test_take_random_returns_random_tile():
    tileCollection = TileCollection()
    tileCollection.add_tiles("red", 1000)
    tileCollection.add_tiles("blue", 5)

    with mock.patch('random.choice', choose_blue):
        assert tileCollection.take_random() == "blue"
    