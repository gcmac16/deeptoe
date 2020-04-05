import pytest

from ..cell import Cell
from ..exceptions import CellOccupiedError


def test_is_empty():
    c = Cell('00')
    assert c.is_empty

    c.move('X')
    assert not c.is_empty


def test_str():
    c = Cell('00')
    assert str(c) == '-'

    c.move('X')
    assert str(c) == 'X'


def test_error_on_double_play():
    c = Cell('00')
    c.move('X')

    with pytest.raises(CellOccupiedError):
        c.move('O')


def test_bad_input_error():
    c = Cell('00')

    with pytest.raises(ValueError):
        c.move('BAD INPUT')


def test_cells_equal():
    c = Cell('00')
    c.move('X')

    c2 = Cell('01')
    c2.move('O')

    c3 = Cell('02')
    c4 = Cell('10')
    c4.move('X')

    assert c == c4
    assert not c == c2
    assert not c == c3
    assert not c2 == c3

   
