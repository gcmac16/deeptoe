from .exceptions import CellOccupiedError


class Cell(object):
    """
    A cell object is the base container for tic tac toe boards.
    Its main functions are validating that plays happen on empty
    cells as well as providing a clean way for boards to check
    their state.
    """

    def __init__(self, cell_id: str):
        self.id = cell_id
        self.value = None

    def move(self, symbol: str):
        if not self.is_empty:
            raise CellOccupiedError(f"Cell {self.id} is occupied")

        if symbol not in ('X', 'O'):
            raise ValueError("Must play an 'X' or 'O'")

        self.value = symbol

    @property
    def is_empty(self):
        return self.value is None

    def __str__(self):
        if self.is_empty:
            return '-'
        return self.value

    def __eq__(self, other_cell):
        if self.is_empty or other_cell.is_empty:
            return False
        return self.value == other_cell.value
