class TileWall():
    def __init__(self):
        colors = ["blue", "yellow", "red", "black", "teal"]
        self.tile_wall = [
            [colors[0], colors[1], colors[2], colors[3], colors[4]],
            [colors[4], colors[0], colors[1], colors[2], colors[3]],
            [colors[3], colors[4], colors[0], colors[1], colors[2]],
            [colors[2], colors[3], colors[4], colors[0], colors[1]],
            [colors[1], colors[2], colors[3], colors[4], colors[0]]
        ]
        self.score = 0

    def add_tile(self, row, color):
        row = self.tile_wall[row - 1]
        row_index = self.tile_wall.index(row)

        for i in range(len(row)):
            if row[i] == color:
                row[i] = "filled"
                self.score += 1
                element_index = i

                # add extra point if tile to the right and below, top corner
                if element_index == 0 and self.tile_wall.index(row) == 0:
                    if self.tile_wall[row_index][i + 1] == "filled" and self.tile_wall[row_index + 1][i] == "filled":
                        self.score += 1

                # add extra point if tile to the right and above, below corner
                if element_index == 0 and self.tile_wall.index(row) == 4:
                    if self.tile_wall[row_index][i + 1] == "filled" and self.tile_wall[row_index - 1][i] == "filled":
                        self.score += 1

                # add extra point if tile to the left and below, top corner
                if element_index == 4 and self.tile_wall.index(row) == 0:
                    if self.tile_wall[row_index][i - 1] == "filled" and self.tile_wall[row_index + 1][i] == "filled":
                        self.score += 1

                # add extra point if tile to the left and above, bottom corner
                if element_index == 4 and self.tile_wall.index(row) == 4:
                    if self.tile_wall[row_index][i - 1] == "filled" and self.tile_wall[row_index - 1][i] == "filled":
                        self.score += 1

                # add extra point if tile to the right and tile below or above in range of column, left column
                if element_index == 0 and (self.tile_wall.index(row) > 0 and self.tile_wall.index(row) < 4):
                    if self.tile_wall[row_index][i + 1] == "filled" and (self.tile_wall[row_index - 1][i] == "filled" or self.tile_wall[row_index + 1][i] == "filled"):
                        self.score += 1

                # add extra point if tile to the left and tile below or above in range of column, right coloumn
                if element_index == 4 and (self.tile_wall.index(row) > 0 and self.tile_wall.index(row) < 4):
                    if self.tile_wall[row_index][i - 1] == "filled" and (self.tile_wall[row_index - 1][i] == "filled" or self.tile_wall[row_index + 1][i] == "filled"):
                        self.score += 1

                # add extra point if tile below and tile to the left or right in range of row, top row
                if (element_index > 0 and element_index < 4) and self.tile_wall.index(row) == 0:
                    if self.tile_wall[row_index + 1 ][i] == "filled" and (self.tile_wall[row_index][i + 1] == "filled" or self.tile_wall[row_index - 1][i] == "filled"):
                        self.score += 1

                # add extra point if tile above and tile to the left or right in range of row, bottom row
                if (element_index > 0 and element_index < 4) and self.tile_wall.index(row) == 4:
                    if self.tile_wall[row_index - 1 ][i] == "filled" and (self.tile_wall[row_index][i + 1] == "filled" or self.tile_wall[row_index - 1][i] == "filled"):
                        self.score += 1

                # add extra point if tile to the right or left and tile below or above in range of row and range of column, inner spaces in tile_wall
                if (element_index > 0 and element_index < 4) and (self.tile_wall.index(row) > 0 and self.tile_wall.index(row) < 4):
                    if (self.tile_wall[row_index][i + 1] == "filled" or self.tile_wall[row_index][i - 1] == "filled") and (self.tile_wall[row_index + 1][i] == "filled" or self.tile_wall[row_index - 1][i] == "filled"):
                        self.score += 1
                                
                while row_index != 0:
                    row_index -= 1
                    if self.tile_wall[row_index][i] == "filled":
                        self.score += 1
                    else:
                        break
                
                row_index = self.tile_wall.index(row)
                while row_index != 4:
                    row_index += 1
                    if self.tile_wall[row_index][i] == "filled":
                        self.score += 1
                    else:
                        break
                
                row_index = self.tile_wall.index(row)
                while i != 0:
                    i -= 1
                    if self.tile_wall[row_index][i] == "filled":
                        self.score += 1
                    else:
                        break

                i = element_index
                while i != 4:
                    i += 1
                    if self.tile_wall[row_index][i] == "filled":
                        self.score += 1
                    else:
                        break

        return self.score
