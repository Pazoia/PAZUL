from pazul.tile_wall import TileWall

def test_add_tile_to_tile_wall():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(1, "red")
    assert tile_wall.tile_wall[0].get_slot_by_color("red").filled
    
def test_resolving_score_from_tile_with_no_tiles_next_to_it():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    assert tile_wall.score == 1

def test_resolving_score_from_one_tile_below():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    tile_wall.add_tile_to_tile_wall(2, "yellow")
    assert tile_wall.score == 3

def test_resolving_score_from_one_tile_above():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    tile_wall.add_tile_to_tile_wall(4, "teal")
    assert tile_wall.score == 3

def test_resolving_score_from_one_tile_below_and_one_tile_above():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(2, "yellow")
    tile_wall.add_tile_to_tile_wall(4, "teal")
    tile_wall.add_tile_to_tile_wall(3, "blue")
    assert tile_wall.score == 5

def test_resolving_score_from_many_tiles_below():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    tile_wall.add_tile_to_tile_wall(4, "teal")
    tile_wall.add_tile_to_tile_wall(5, "black")
    tile_wall.add_tile_to_tile_wall(2, "yellow")
    assert tile_wall.score == 10

def test_resolving_score_from_many_tiles_above():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    tile_wall.add_tile_to_tile_wall(2, "yellow")
    tile_wall.add_tile_to_tile_wall(1, "red")
    tile_wall.add_tile_to_tile_wall(4, "teal")
    assert tile_wall.score == 10

def test_resolving_score_from_many_tiles_below_and_many_tiles_above():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(2, "yellow")
    tile_wall.add_tile_to_tile_wall(1, "red")
    tile_wall.add_tile_to_tile_wall(4, "teal")
    tile_wall.add_tile_to_tile_wall(5, "black")
    tile_wall.add_tile_to_tile_wall(3, "blue")
    assert tile_wall.score == 11

def test_resolving_score_from_one_tile_to_the_right():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    tile_wall.add_tile_to_tile_wall(3, "teal")
    assert tile_wall.score == 3

def test_resolving_score_from_one_tile_the_left():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    tile_wall.add_tile_to_tile_wall(3, "yellow")
    assert tile_wall.score == 3

def test_resolving_score_from_one_tile_the_left_and_one_tile_to_the_right():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "teal")
    tile_wall.add_tile_to_tile_wall(3, "yellow")
    tile_wall.add_tile_to_tile_wall(3, "blue")
    assert tile_wall.score == 5

def test_resolving_score_from_many_tiles_to_the_left():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    tile_wall.add_tile_to_tile_wall(3, "teal")
    tile_wall.add_tile_to_tile_wall(3, "black")
    tile_wall.add_tile_to_tile_wall(3, "yellow")
    assert tile_wall.score == 10

def test_resolving_score_from_many_tiles_to_the_right():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "blue")
    tile_wall.add_tile_to_tile_wall(3, "yellow")
    tile_wall.add_tile_to_tile_wall(3, "red")
    tile_wall.add_tile_to_tile_wall(3, "teal")
    assert tile_wall.score == 10

def test_resolving_score_from_many_tiles_to_the_right_and_many_tiles_to_the_left():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "teal")
    tile_wall.add_tile_to_tile_wall(3, "black")
    tile_wall.add_tile_to_tile_wall(3, "yellow")
    tile_wall.add_tile_to_tile_wall(3, "red")
    tile_wall.add_tile_to_tile_wall(3, "blue")
    assert tile_wall.score == 11

def test_resolving_score_from_one_tile_the_left_and_one_tile_on_top():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(4, "yellow")
    tile_wall.add_tile_to_tile_wall(5, "teal")
    tile_wall.add_tile_to_tile_wall(5, "blue")
    assert tile_wall.score == 6

def test_resolving_score_from_one_tile_the_left_and_one_tile_on_bottom():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(1, "black")
    tile_wall.add_tile_to_tile_wall(2, "black")
    tile_wall.add_tile_to_tile_wall(1, "teal")
    assert tile_wall.score == 6

def test_resolving_score_from_one_tile_the_right_and_one_tile_on_top():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(5, "red")
    tile_wall.add_tile_to_tile_wall(4, "red")
    tile_wall.add_tile_to_tile_wall(5, "yellow")
    assert tile_wall.score == 6

def test_resolving_score_from_one_tile_the_right_and_one_tile_on_bottom():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(1, "yellow")
    tile_wall.add_tile_to_tile_wall(2, "teal")
    tile_wall.add_tile_to_tile_wall(1, "blue")
    assert tile_wall.score == 6

def test_resolving_score_from_tiles_left_right_above_below():
    tile_wall = TileWall()
    tile_wall.add_tile_to_tile_wall(3, "teal")
    tile_wall.add_tile_to_tile_wall(3, "yellow")
    tile_wall.add_tile_to_tile_wall(4, "teal")
    tile_wall.add_tile_to_tile_wall(2, "yellow")
    tile_wall.add_tile_to_tile_wall(3, "blue")
    assert tile_wall.score == 10

def test_resolving_score_stops_on_blank_space_column():
    tile_wall = TileWall()
    assert tile_wall.add_tile_to_tile_wall(1, "blue") == 1
    assert tile_wall.add_tile_to_tile_wall(2, "teal") == 2
    assert tile_wall.add_tile_to_tile_wall(4, "red") == 1
    assert tile_wall.score == 4

def test_resolving_score_stops_on_blank_space_row():
    tile_wall = TileWall()
    assert tile_wall.add_tile_to_tile_wall(3, "teal") == 1
    assert tile_wall.add_tile_to_tile_wall(3, "black") == 2
    assert tile_wall.add_tile_to_tile_wall(3, "yellow") == 1
    assert tile_wall.score == 4

