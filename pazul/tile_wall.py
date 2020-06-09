from collections import deque

class WallSlot():
    def __init__(self, color, index):
        self.color = color
        self.filled = False
        self.index = index


class WallRow():
    def __init__(self, colors):
        self.row = []
        for i in range(len(colors)):
            self.row.append(WallSlot(colors[i], i))

    def __str__(self):
        out = ""
        for slot in self.row:
            out += f"[{slot.color}]"
        return out

    def get_slot_by_color(self, color):
        for slot in self.row:
            if slot.color == color:
                return slot
        # Could throw here, if asked for a colour that doesn't exist?

    def get_slot_by_index(self, index):
        # Could check not asking for index out of bounds?
        return self.row[index]


class TileWall():
    def __init__(self):
        colors = deque(["blue", "yellow", "red", "black", "teal"])
        self.tile_wall = []
        self.score = 0
        for _ in range(5):
            # Add a row
            self.tile_wall.append(WallRow(colors))
            # Rotate the colors
            colors.rotate(1)

    def __str__(self):
        out = ""
        for row in self.tile_wall:
            out += str(row) + "\n"
        return out

    def add_tile_to_tile_wall(self, row, color):
        row_index = row - 1
        row = self.tile_wall[row_index]
        slot = row.get_slot_by_color(color)
        slot.filled = True
        score = 1
        slot_above_or_below_filled = False
        slot_right_or_slot_left_filled = False

        # check before the slot and add points. Break if we find an epty slot.
        for i in range(slot.index - 1, -1, -1):
            slot_to_check = row.get_slot_by_index(i)
            if slot_to_check.filled:
                slot_right_or_slot_left_filled = True
                score += 1
            else:
                break

        # check after the slot...
        for i in range(slot.index + 1, 5):
            slot_to_check = row.get_slot_by_index(i)
            if slot_to_check.filled:
                slot_right_or_slot_left_filled = True
                score += 1
            else:
                break

        # check above the slot...
        for i in range(row_index - 1, -1, -1):
            row_to_check = self.tile_wall[i]
            slot_to_check = row_to_check.get_slot_by_index(slot.index)
            if slot_to_check.filled:
                slot_above_or_below_filled = True
                score += 1
            else:
                break

        # check below the slot...
        for i in range(row_index + 1, 5):
            row_to_check = self.tile_wall[i]
            slot_to_check = row_to_check.get_slot_by_index(slot.index)
            if slot_to_check.filled:
                slot_above_or_below_filled = True
                score += 1
            else:
                break
        
        if slot_right_or_slot_left_filled and slot_above_or_below_filled:
            score += 1

        self.score += score
        return score
