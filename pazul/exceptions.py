class Error(Exception):
    pass

class EmptyTileCollectionError(Error):
    def __init__(self):
        self.message = "Tile collection empty, cannot remove tiles"

class InvalidColor(Error):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)