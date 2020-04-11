from typing import (
    List,
    Tuple,
)
from numpy.random import choice

from .ultimate_board import UltimateBoard


class Game(object):
    
    def __init__(self, cpu_mode: str = 'random'):
        self.board = UltimateBoard()
        self.cpu_mode = cpu_mode
        self.n_moves = 0
        
    def player_move(self, board_id: str, cell_id: str):
        self.board.move(board_id, cell_id, 'X')
        self.n_moves += 1
        print('----------- Player Move --------------')
        print(self.__str__())
        print(f'After Turn: Player {self.board.turn}s Turn') 
        print()
            
    def computer_move(self) -> Tuple[str]:
        if self.cpu_mode == 'random':
            # get random board
            random_board_id = choice(list(self.board.active_boards), size=1)[0]
            random_board = self.board.boards[random_board_id]
            random_cell_id = choice(random_board.get_empty_cell_ids(), size=1)[0]
            self.board.move(random_board_id, random_cell_id, 'O')
            self.n_moves += 1
            
            print('----------- Computer Move --------------')
            print(self.__str__())
            print()
            
            return random_board_id, random_cell_id
        else:
            pass
        
    def get_cell_values(self) -> List[str]:
        cell_values = []
        for board in self.board.boards.values():
            for cell in board.board.values():
                cell_values.append(
                    cell.value if cell.value in ('X', 'O')
                    else ''
                )
                
        return cell_values
      
    def __str__(self) -> str:
        return str(self.board)
    
    def __repr__(self) -> str:
        return self.__str__()