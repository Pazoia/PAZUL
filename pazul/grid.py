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
                element_index = i

                # add extra point if tile to the right and below top corner
                if element_index == 0 and self.grid.index(row) == 0:
                    if self.grid[row_index][i + 1] == "filled" and self.grid[row_index + 1][i] == "filled":
                        self.score += 1
                        print("add extra point if tile to the right and below top corner")

                # add extra point if tile to the right and above below corner
                if element_index == 0 and self.grid.index(row) == 4:
                    if self.grid[row_index][i + 1] == "filled" and self.grid[row_index - 1][i] == "filled":
                        self.score += 1
                        print("add extra point if tile to the right and above below corner")

                # add extra point if tile to the left and below top corner
                if element_index == 4 and self.grid.index(row) == 0:
                    if self.grid[row_index][i - 1] == "filled" and self.grid[row_index + 1][i] == "filled":
                        self.score += 1
                        print("add extra point if tile to the left and below top corner")

                # add extra point if tile to the left and above bottom corner
                if element_index == 4 and self.grid.index(row) == 4:
                    if self.grid[row_index][i - 1] == "filled" and self.grid[row_index - 1][i] == "filled":
                        self.score += 1
                        print("add extra point if tile to the left and above bottom corner")

                # add extra point if tile to the right and tile below or above in range of column
                if element_index == 0 and (self.grid.index(row) > 0 and self.grid.index(row) < 4):
                    if self.grid[row_index][i + 1] == "filled" and (self.grid[row_index - 1][i] == "filled" or self.grid[row_index + 1][i] == "filled"):
                        self.score += 1
                        print("add extra point if tile to the right and tile below in range of column")

                # add extra point if tile to the left and tile below or above in range of column
                if element_index == 4 and (self.grid.index(row) > 0 and self.grid.index(row) < 4):
                    if self.grid[row_index][i - 1] == "filled" and (self.grid[row_index - 1][i] == "filled" or self.grid[row_index + 1][i] == "filled"):
                        self.score += 1
                        print("add extra point if tile to the left and tile below in range of column")

                # add extra point if tile below and tile to the left or right in range of row
                if (element_index > 0 and element_index < 4) and self.grid.index(row) == 0:
                    if self.grid[row_index + 1 ][i] == "filled" and (self.grid[row_index][i + 1] == "filled" or self.grid[row_index - 1][i] == "filled"):
                        self.score += 1
                        print("add extra point if tile below and tile to the left or right in range of row")

                # add extra point if tile above and tile to the left or right in range of row
                if (element_index > 0 and element_index < 4) and self.grid.index(row) == 4:
                    if self.grid[row_index - 1 ][i] == "filled" and (self.grid[row_index][i + 1] == "filled" or self.grid[row_index - 1][i] == "filled"):
                        self.score += 1
                        print("add extra point if tile above and tile to the left or right in range of row")

                # add extra point if tile to the right or left and tile below or above in range of row and range of column
                if (element_index > 0 and element_index < 4) and (self.grid.index(row) > 0 and self.grid.index(row) < 4):
                    if (self.grid[row_index][i + 1] == "filled" or self.grid[row_index][i - 1] == "filled") and (self.grid[row_index + 1][i] == "filled" or self.grid[row_index - 1][i] == "filled"):
                        self.score += 1
                        print("add extra point if tile to the right and tile below in range of row and range of column")
                                
                while row_index != 0:
                    row_index -= 1
                    if self.grid[row_index][i] == "filled":
                        self.score += 1
                        print("point from tile above")
                    else:
                        break
                
                row_index = self.grid.index(row)
                while row_index != 4:
                    row_index += 1
                    if self.grid[row_index][i] == "filled":
                        self.score += 1
                        print("point from tile below")
                    else:
                        break
                
                row_index = self.grid.index(row)
                while i != 0:
                    i -= 1
                    if self.grid[row_index][i] == "filled":
                        self.score += 1
                        print("point from left tile")
                    else:
                        break

                i = element_index
                while i != 4:
                    i += 1
                    if self.grid[row_index][i] == "filled":
                        self.score += 1
                        print("point from right tile")
                    else:
                        break

        print(f"score = {self.score}")

grid = Grid()
grid.add_tile(1, "yellow")
grid.printing_grid()
print("- - - - - - - - -")
grid.add_tile(1, "black")
grid.printing_grid()
print("- - - - - - - - -")
grid.add_tile(2, "yellow")
grid.printing_grid()
print("- - - - - - - - -")
grid.add_tile(1, "red")
grid.printing_grid()
print("- - - - - - - - -")
# grid.add_tile(3, "blue")
# grid.printing_grid()
# print("- - - - - - - - -")
# grid.add_tile(3, "black")
# grid.printing_grid()
# print("- - - - - - - - -")
# grid.add_tile(3, "yellow")
# grid.printing_grid()
# print("- - - - - - - - -")
# grid.add_tile(3, "red")
# grid.printing_grid()
# print("- - - - - - - - -")
# grid.add_tile(3, "blue")
# grid.printing_grid()
# print("- - - - - - - - -")
