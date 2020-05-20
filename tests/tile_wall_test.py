from pazul.tile_wall import TileWall

def test_add_tile():
    tile_wall = TileWall()
    tile_wall.add_tile(1, "red")
    assert tile_wall.tile_wall[0][2] == "filled"

def test_resolving_score_place_tile_with_no_tiles_next_to_it():
    tile_wall = TileWall()
    tile_wall.add_tile(1, "red")
    assert tile_wall.score == 1

def test_resolving_score_place_tile_below_another():
    tile_wall = TileWall()
    tile_wall.add_tile(1, "red")
    tile_wall.add_tile(2, "yellow")
    assert tile_wall.score == 3

def test_resolving_score_place_tile_above_another():
    tile_wall = TileWall()
    tile_wall.add_tile(2, "yellow")
    tile_wall.add_tile(1, "red")
    assert tile_wall.score == 3

def test_resolving_score_place_tile_above_multiple_tiles():
    tile_wall = TileWall()
    tile_wall.add_tile(3, "yellow")
    tile_wall.add_tile(4, "blue")
    tile_wall.add_tile(5, "teal")
    tile_wall.add_tile(2, "red")
    assert tile_wall.score == 10

def test_resolving_score_place_tile_below_multiple_tiles():
    tile_wall = TileWall()
    tile_wall.add_tile(4, "black")
    tile_wall.add_tile(3, "teal")
    tile_wall.add_tile(2, "blue")
    tile_wall.add_tile(5, "red")
    assert tile_wall.score == 10

# write tests for horizontal scorings