class Grid():
    def __init__(self):
        colors = ["blue", "yellow", "red", "black", "teal"]
        self.score = 0

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
        row_index = self.grid.index(row)

        for i in range(len(row)):
            if row[i] == color:
                row[i] = "filled"
                self.score += 1
                print("adding 1 point from tile placement")

                while row_index - 1 != -1:
                    row_index -= 1
                    if self.grid[row_index][i] == "filled":
                        self.score += 1
                        print("adding extra point from tile above")
                    else:
                        break
                row_index = self.grid.index(row)
                while row_index + 1 != 5:
                    row_index += 1
                    if self.grid[row_index][i] == "filled":
                        self.score += 1
                        print("adding extra point from tile below")
                    else:
                        break

        print(f"score = {self.score}")

        # resolve the scores, check filled spaces near tile
        # returns points scored by tile

grid = Grid()
grid.add_tile(1, "red")
grid.printing_grid()
grid.add_tile(2, "yellow")
grid.printing_grid()
grid.add_tile(5, "black")
grid.printing_grid()
grid.add_tile(4, "teal")
grid.printing_grid()
grid.add_tile(3, "blue")
grid.printing_grid()
