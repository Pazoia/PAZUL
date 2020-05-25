class BuildingRows:
    def __init__(self):
        self.building_rows = []
        slots = 1
        
        for _ in range(5):
            row = [None] * slots
            self.building_rows.append(row)
            slots = slots + 1

    def add_tiles_to_building_row(self, row, color, quantity):
        row_index = row - 1
        row = self.building_rows[row_index]
        row_length = len(row)
        slots_to_be_filled = quantity

        
        for i in range(row[len(row)-1], -1, -1):            
            if row[len(row)-1] == None:
                row[len(row)-1] = color
                slots_to_be_filled -= 1
            if row[len(row)-1] == color:
                pass

            
build_row = BuildingRows()
print(build_row.building_rows)
build_row.add_tiles_to_building_row(5, "blue", 1)
print(build_row.building_rows)
build_row.add_tiles_to_building_row(5, "blue", 7)
print(build_row.building_rows)
