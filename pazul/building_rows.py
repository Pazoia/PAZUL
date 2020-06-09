from pazul.exceptions import InvalidColor

class Row:
    def __init__(self, capacity):
        self.capacity = capacity
        self.filled_slots = 0
        self.color = None

    def get_remaining_capacity(self):
        return self.capacity - self.filled_slots

    def get_color(self):
        return self.color

    def add_tiles(self, color, quantity):
        if self.color != None and self.color != color:
            raise InvalidColor(f"Row already has {self.color} tiles, cannot add {color} tiles.")
        self.color = color

        overflow_tiles = quantity - self.get_remaining_capacity()
        if overflow_tiles < 0:
            overflow_tiles = 0

        used_tiles = quantity - overflow_tiles
        self.filled_slots += used_tiles
        return overflow_tiles


class BuildingRows:
    def __init__(self):
        self.building_rows = []
        for i in range(5):
            self.building_rows.append(Row(i + 1))

    def add_tiles_to_building_row(self, row, color, quantity):
        row_index = row -1
        row = self.building_rows[row_index]
        tiles_not_used = row.add_tiles(color, quantity)
        return tiles_not_used
