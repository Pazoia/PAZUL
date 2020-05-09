class Error(Exception):
    pass

class EmptyTileCollectionError(Error):
    def __init__(self):
        self.message = "Tile collection empty, cannot remove tiles"
