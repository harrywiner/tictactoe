from pydantic import BaseModel
from minimax import get_best_move
import re
class Human:
    def get_move(self, board):
        valid = False
        while (not valid):
            move = input("What is your move?\n")

            if re.match("\d\,\d", move):
                next_move = (int(move[0]), int(move[2]))
                valid = True
            else:
                print("invalid please use format \d\,\d")
        return next_move
    
class Minimax:
    def get_move(self, board):
        move, p_eval = get_best_move(board)
        print(f"Computer eval: {p_eval.score}; Nodes searched: {p_eval.nodes}")
        return move
    
    
class QLearn:
    def get_move(self, board):
        pass