import sys
sys.path.append("src")

from tile_collection import *

def test_func():
  result = TileCollection.func(3)
  assert result == 4

def test_add():
  sum = TileCollection.add(3, 5)
  assert sum == 8
