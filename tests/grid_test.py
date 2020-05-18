from pazul.grid import Grid

def test_add_tile():
    grid = Grid()
    grid.add_tile(1, "red")
    assert grid.grid[0][2] == "filled"