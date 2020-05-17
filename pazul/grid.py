class Grid():
    def __init__(self):
        COLORS = ["blue", "yellow", "red", "black", "teal"]

        self.grid = [
            [colors[0], colors[1], colors[2], colors[3], colors[4]],
            [colors[4], colors[0], colors[1], colors[2], colors[3]],
            [colors[3], colors[4], colors[0], colors[1], colors[2]],
            [colors[2], colors[3], colors[4], colors[0], colors[1]],
            [colors[1], colors[2], colors[3], colors[4], colors[0]]
        ]

    def printing_grid(self):
        for row in self.grid:
            print(row)

    def add_tile(self, row, color):
        row = self.grid[row - 1]
        print(f"selected row = {row}")
        # returns points scored by tile

grid = Grid()
grid.printing_grid()
grid.add_tile(3, "blue")