import pytest
from pazul.building_rows import BuildingRows
from pazul.exceptions import InvalidColor

def test_add_one_tile_to_an_empty_row():
    building_rows = BuildingRows()
    building_rows.add_tiles_to_building_row(1, "blue", 1)
    assert building_rows.building_rows[0][-1] == "blue"

def test_add_many_tiles_to_empty_row():
    building_rows = BuildingRows()
    building_rows.add_tiles_to_building_row(3, "blue", 3)
    assert building_rows.building_rows[2].count("blue") == 3

def test_add_one_tile_to_non_empty_row():
    building_rows = BuildingRows()
    building_rows.add_tiles_to_building_row(2, "blue", 1)
    building_rows.add_tiles_to_building_row(2, "blue", 1)
    assert building_rows.building_rows[1].count("blue") == 2

def test_add_many_tiles_to_non_empty_row():
    building_rows = BuildingRows()
    building_rows.add_tiles_to_building_row(4, "blue", 1)
    building_rows.add_tiles_to_building_row(4, "blue", 3)
    assert building_rows.building_rows[3].count("blue") == 4

def test_too_many_tiles_for_row_size_returning_tiles_not_used():
    building_rows = BuildingRows()
    building_rows.add_tiles_to_building_row(4, "blue", 1)
    assert building_rows.add_tiles_to_building_row(4, "blue", 5) == 2

def test_add_tile_of_different_color_to_color_in_row():
    with pytest.raises(InvalidColor):
        building_rows = BuildingRows()
        building_rows.add_tiles_to_building_row(4, "blue", 3)
        building_rows.add_tiles_to_building_row(4, "red", 1)

def test_add_tile_of_different_color_to_color_in_full_row():
    with pytest.raises(InvalidColor):
        building_rows = BuildingRows()
        building_rows.add_tiles_to_building_row(1, "blue", 1)
        building_rows.add_tiles_to_building_row(1, "red", 1)
