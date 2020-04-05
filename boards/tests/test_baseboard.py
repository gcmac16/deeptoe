import pytest

from ..baseboard import BaseBoard
from ..exceptions import (
    CellOccupiedError,
    GameOverError
)


def test_game_over_top_row():
    b = BaseBoard('00')
    b.move('00', 'X')
    b.move('01', 'X')
    b.move('02', 'X')
    
    assert b.game_over
    assert b.winner == 'X'

    
def test_game_over_middle_row():
    b = BaseBoard('00')
    b.move('10', 'O')
    b.move('11', 'O')
    b.move('12', 'O')
    
    assert b.game_over
    assert b.winner == 'O'

    
def test_game_over_bottom_row():
    b = BaseBoard('00')
    b.move('20', 'O')
    b.move('21', 'O')
    b.move('22', 'O')
    
    assert b.game_over
    assert b.winner == 'O'

    
def test_game_over_left_column():
    b = BaseBoard('00')
    b.move('00', 'X')
    b.move('10', 'X')
    b.move('20', 'X')
    
    assert b.game_over
    assert b.winner == 'X'

    
def test_game_over_middle_column():
    b = BaseBoard('00')
    b.move('01', 'X')
    b.move('11', 'X')
    b.move('21', 'X')
    
    assert b.game_over
    assert b.winner == 'X'

    
def test_game_over_right_column():
    b = BaseBoard('00')
    b.move('02', 'O')
    b.move('12', 'O')
    b.move('22', 'O')
    
    assert b.game_over
    assert b.winner == 'O'

    
def test_game_over_diag1():
    b = BaseBoard('00')
    b.move('00', 'O')
    b.move('11', 'O')
    b.move('22', 'O')
    
    assert b.game_over
    assert b.winner == 'O'

    
def test_game_over_diag2():
    b = BaseBoard('00')
    b.move('02', 'O')
    b.move('11', 'O')
    b.move('20', 'O')
    
    assert b.game_over
    assert b.winner == 'O'
    
    
def test_game_over_raise_error():
    b = BaseBoard('00')
    b.move('02', 'O')
    b.move('11', 'O')
    b.move('20', 'O')
    
    assert b.game_over
    assert b.winner == 'O'
    
    with pytest.raises(GameOverError):
        b.move('12', 'X')
        

def test_cat_game():
    b = BaseBoard('00')
    b.move('00', 'O')
    b.move('01', 'X')
    b.move('02', 'O')
    b.move('10', 'X')
    b.move('11', 'O')
    b.move('12', 'X')
    b.move('20', 'X')
    b.move('21', 'O')
    b.move('22', 'X')
    
    assert b.game_over
    assert b.winner == 'CAT'
    

def test_double_move():
    b = BaseBoard('00')
    b.move('00', 'X')
    
    with pytest.raises(CellOccupiedError):
        b.move('00', 'O')