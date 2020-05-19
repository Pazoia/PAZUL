from pazul.grid import Grid

def test_add_tile():
    grid = Grid()
    grid.add_tile(1, "red")
    assert grid.grid[0][2] == "filled"

def test_resolving_score_place_tile_with_no_tiles_next_to_it():
    grid = Grid()
    grid.add_tile(1, "red")
    assert grid.score == 1

def test_resolving_score_place_tile_below_another():
    grid = Grid()
    grid.add_tile(1, "red")
    grid.add_tile(2, "yellow")
    assert grid.score == 3

def test_resolving_score_place_tile_above_another():
    grid = Grid()
    grid.add_tile(2, "yellow")
    grid.add_tile(1, "red")
    assert grid.score == 3

def test_resolving_score_place_tile_above_multiple_tiles():
    grid = Grid()
    grid.add_tile(3, "yellow")
    grid.add_tile(4, "blue")
    grid.add_tile(5, "teal")
    grid.add_tile(2, "red")
    assert grid.score == 10

def test_resolving_score_place_tile_below_multiple_tiles():
    grid = Grid()
    grid.add_tile(4, "black")
    grid.add_tile(3, "teal")
    grid.add_tile(2, "blue")
    grid.add_tile(5, "red")
    assert grid.score == 10

# write tests for horizontal scorings