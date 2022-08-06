from computer_player import get_best_move
from library import Board
import re

COMPUTER = 0
HUMAN = 1

if __name__ == "__main__":
    board = Board()
    PLAYER_ONE = HUMAN
    PLAYER_TWO = COMPUTER
    
    while (board.result() == board.NO_RESULT):
        next_move = (0,0)
        if board.to_move() == board.PLAYER_X:
            valid = False
            while (not valid):
                move = input("What is your move?")

                if re.match("\d\,\d", move):
                   next_move = (int(move[0]), int(move[2]))
                   valid = True
                else:
                    print("invalid please use format \d\,\d")
            
            
        else:
            get_best_move(board)
            
    
    pass