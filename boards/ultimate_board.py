from typing import (
    Dict,
    Tuple,
    Union
)

from .exceptions import (
    InactiveBoardError,
    GameOverError,
    WrongTurnError
)
from .baseboard import BaseBoard


class UltimateBoard(object):
    
    def __init__(self):
        self.turn = 'X'
        self.n_moves = 0
        self.game_over = False
        self.boards = self._initialize_boards()
        self.active_boards = self.boards.keys()
        
        
    @staticmethod
    def _initialize_boards() -> Dict[str, str]:
        new_board = {}
        for i in range(3):
            for j in range(3):
                # each cell in the ultimate board is itself a baseboard
                new_board[f'{i}{j}'] = BaseBoard(f'{i}{j}')
                
        return new_board
    
    def move(self, board_id: str, cell_id: str, symbol: str) -> None:
        self.validate_move(board_id, symbol)
        self.boards[board_id].move(cell_id, symbol)
        self.n_moves += 1
        
        # check if the game's over and find the winner if its
        self.game_over, winner = self.check_game_over() 
        if self.game_over:
            self.winner = winner
            return
        
        # if game isn't over, update state for next turn
        self.turn = self.flip_turn()
        self.update_active_boards(board_id, cell_id)
        
    def update_active_boards(self, board_id: str, cell_id:str) -> None:
        """
        Logic for updating the active boards the next player can play on.
        If the board at the cell location of the last player's move still
        has an active game, that's the only active board. If that board's
        game is over, all boards that still have a live game are active.
        """
        if not self.boards[cell_id].game_over:
            self.active_boards = [cell_id]
        else:
            self.active_boards = [
                board_id for board_id, board in self.boards.items()
                if not board.game_over
            ]
            
    def check_game_over(self) -> Tuple[bool, Union[str, None]]:
        winning_board_combinations = (
            ('00', '01', '02'),
            ('10', '11', '12'),
            ('20', '21', '22'),
            ('00', '10', '20'),
            ('01', '11', '21'),
            ('02', '12', '22'),
            ('00', '11', '22'),
            ('20', '11', '02')
        )
        
        for board_1, board_2, board_3 in winning_board_combinations:
            if (
                self.boards[board_1].game_over 
                and self.boards[board_2].game_over 
                and self.boards[board_3] 
                and self.boards[board_1].winner == self.boards[board_2].winner == self.boards[board_3].winner
            ):
                return True, self.boards[board_1].winner
        
        if self.n_moves == 81:
            return True, 'CAT'
        
        return False, None
        
    def validate_move(self, board_id: str, symbol: str) -> None:
        if symbol != self.turn:
            raise WrongTurnError(f"It is player {self.turn}'s turn, not {symbol}'")
                                 
        if board_id not in self.active_boards:
            message = f"Board {board_id} is inactive. Active boards are {self.active_boards}"
            raise InactiveBoardError(message)
                                
        if self.game_over:
            raise GameOverError(f"Game on board{self.id} is over")
        
    def flip_turn(self) -> None:
        if self.turn == 'X':
            return 'O'

        if self.turn == 'O':
            return 'X'