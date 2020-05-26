import numpy
from pazul.exceptions import InvalidColor

class BuildingRows:
    def __init__(self):
        # self.building_rows = numpy.empty(shape=(5, 1),dtype='object')
        self.building_rows = [[],[],[],[],[]]

    def add_tiles_to_building_row(self, row, color, quantity):
        row_index = row - 1
        row = self.building_rows[row_index]
        tiles_placed = 0

        for _ in range(quantity):
            if len(row) == row_index + 1:
                tiles_not_used = quantity - tiles_placed
                print(f"tiles not used: {tiles_not_used}")
                return tiles_not_used

            if len(row) == 0:
                row.append(color)
                tiles_placed += 1
            elif len(row) != 0 and row.count(color) == len(row):
                row.append(color)
                tiles_placed += 1
            else:
                raise InvalidColor("Chosen color not matching existing color")
