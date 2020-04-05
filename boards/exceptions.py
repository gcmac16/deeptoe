class Error(Exception):
    """Base class for other exceptions"""
    pass


class GameOverError(Error):
    """Raised when the game on a particular board is over"""
    pass


class CellOccupiedError(Error):
    """Raised when a move is played in a non-empty cell"""
