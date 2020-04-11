from typing import (
    Dict,
    List,
    Tuple,
    Union,
)

from .cell import Cell
from .exceptions import GameOverError


class BaseBoard(object):
    
    def __init__(self, board_id: str):
        self.board = self._initialize_board()
        self.id = board_id
        self.game_over = False
        self.winner = ''
        self.n_moves = 0
        
    @staticmethod
    def _initialize_board() -> Dict[str, str]:
        new_board = {}
        for i in range(3):
            for j in range(3):
                new_board[f'{i}{j}'] = Cell(f'{i}{j}')
                
        return new_board
    
    def move(self, cell_id: str, symbol: str) -> None:
        self.validate_move(cell_id)
        self.board[cell_id].move(symbol)
        self.n_moves += 1
        self.game_over, winner = self.check_game_over()   
        
        if self.game_over:
            self.winner = winner
        
    def validate_move(self, cell_id: str) -> None:
        if self.game_over:
            raise GameOverError(f"Game on board{self.id} is over")
    
    def check_game_over(self) -> Tuple[bool, Union[str, None]]:
        winning_cell_combinations = (
            ('00', '01', '02'),
            ('10', '11', '12'),
            ('20', '21', '22'),
            ('00', '10', '20'),
            ('01', '11', '21'),
            ('02', '12', '22'),
            ('00', '11', '22'),
            ('20', '11', '02')
        )
        
        for cell_1, cell_2, cell_3 in winning_cell_combinations:
            if self.board[cell_1] == self.board[cell_2] == self.board[cell_3]:
                return True, self.board[cell_1].value
        
        if self.n_moves == 9:
            return True, 'CAT'
        
        return False, None
    
    def get_empty_cell_ids(self) -> List[Cell]:
        return [
            cell_id for cell_id, cell in self.board.items()
            if cell.is_empty
        ]
        
    def __str__(self) -> str:
        rows = (
            ('00', '01', '02'),
            ('10', '11', '12'),
            ('20', '21', '22'),
        )
        
        s = []
        for c1, c2, c3 in rows:
            s.append(f'{self.board[c1]} {self.board[c2]} {self.board[c3]}')
            
        return '\n'.join(s)
    
    def __repr__(self) -> str:
        return self.__str__()
    