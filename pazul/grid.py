class Grid():
    def __init__(self):
        self.colors = {
            "blue": 1,
            "yellow": 1,
            "red": 1,
            "black": 1,
            "teal": 1
        }
        self.grid = []

        for column in range(5):
            self.grid.append(list(self.colors.keys()))
        for row in self.grid:
            print(f"row = {row}")
            for i in row:
                print(f"i = {i}")

grid = Grid()
print(grid.grid)