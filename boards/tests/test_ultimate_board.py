import pytest

from ..ultimate_board import UltimateBoard
from ..exceptions import (
    CellOccupiedError,
    GameOverError,
    InactiveBoardError,
    WrongTurnError
)


def test_double_move_fails():
    ub = UltimateBoard()
    ub.move('00', '01', 'X')
    assert ub.turn == 'O'
    
    with pytest.raises(WrongTurnError):
        ub.move('01', '02', 'X')
        
def test_active_boards_basic():
    ub = UltimateBoard()
    ub.move('00', '21', 'X')
    assert ub.active_boards == ['21']
    
    ub.move('21', '12', 'O')
    assert ub.active_boards == ['12']
    
    ub.move('12', '12', 'X')
    assert ub.active_boards == ['12']
    
    
def test_active_boards_advanced():
    ub = UltimateBoard()
    
    # shut off some random boards
    board_ids = ['02', '11', '21']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'X'
        
    ub.move('00', '02', 'X')
    assert ub.active_boards == ['00', '01', '10', '12', '20', '22']
    
    ub.move('22', '01', 'O')
    assert ub.active_boards == ['01']
    
    ub.boards['22'].game_over = True
    ub.move('01', '11', 'X')
    assert ub.active_boards == ['00', '01', '10', '12', '20']
    

def error_on_inactive_board():
    ub = UltimateBoard()
    ub.move('00', '11', 'X')
    
    with pytest.raises(InactiveBoardError):
        ub.move('22', '00', 'O')    
    
def test_game_over_top_row():
    ub = UltimateBoard()
    
    board_ids = ['00', '01', '02']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'X'
        
    game_over, winner = ub.check_game_over()
    assert game_over
    assert winner == 'X'
    
    
def test_game_over_middle_row():
    ub = UltimateBoard()
    
    board_ids = ['10', '11', '12']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'O'
        
    game_over, winner = ub.check_game_over()
    assert game_over
    assert winner == 'O'
    
    
def test_game_over_bottom_row():
    ub = UltimateBoard()
    
    board_ids = ['20', '21', '22']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'X'
        
    game_over, winner = ub.check_game_over()
    assert game_over
    assert winner == 'X'
    
    
def test_game_over_left_column():
    ub = UltimateBoard()
    
    board_ids = ['00', '10', '20']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'X'
        
    game_over, winner = ub.check_game_over()
    assert game_over
    assert winner == 'X'
    
    
def test_game_over_middle_column():
    ub = UltimateBoard()
    
    board_ids = ['01', '11', '21']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'O'
        
    game_over, winner = ub.check_game_over()
    assert game_over
    assert winner == 'O'
    
    
def test_game_over_right_column():
    ub = UltimateBoard()
    
    board_ids = ['02', '12', '22']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'X'
        
    game_over, winner = ub.check_game_over()
    assert game_over
    assert winner == 'X'
    
    
def test_game_over_diag1():
    ub = UltimateBoard()
    
    board_ids = ['00', '11', '22']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'O'
        
    game_over, winner = ub.check_game_over()
    assert game_over
    assert winner == 'O'
    
    
def test_game_over_diag2():
    ub = UltimateBoard()
    
    board_ids = ['02', '11', '20']
    for board_id in board_ids:
        ub.boards[board_id].game_over = True
        ub.boards[board_id].winner = 'X'
        
    game_over, winner = ub.check_game_over()
    assert game_over
    assert winner == 'X'
    
    
def test_baseboard_game_over():
    ub = UltimateBoard()
    ub.move('11', '02', 'X')
    ub.move('02', '11', 'O')
    ub.move('11', '01', 'X')
    ub.move('01', '11', 'O')
    ub.move('11', '00', 'X')
    
    assert ub.boards['11'].game_over
    assert ub.boards['11'].winner == 'X'