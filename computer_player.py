from library import Board, Eval
from typing import List

def get_best_move(board: Board) -> tuple((tuple((int, int)), Eval)):
    moves = board.get_legal_moves()
    best_move = (0, 0)
    best_eval = Eval(score=0,nodes=0)
    for m in moves:
        candidate = board.get_successor(m)
        E = evaluate(candidate)
        if E.score > best_eval.score:
            best_move = m
            best_eval = E
    return best_move, best_eval

def max_agg(evals: List[Eval]) -> Eval:
    maximum = evals[0]
    for e in evals:
        if e.score > maximum.score:
            maximum.score = e.score
        maximum.nodes += e.score
    return maximum
def min_agg(evals: List[Eval]) -> Eval:
    minimum = evals[0]
    for e in evals[1:]:
        if e.score < minimum.score:
            minimum.score = e.score
        minimum.nodes += e.score
    return minimum
def sum_agg(evals: List[Eval]) -> Eval:
    total = evals[0]
    for i in range(1, len(evals)):
        total += evals[i]
    return total

def evaluate(board: Board) -> float:
    result = board.result()
    if result == board.X_WIN:
        return Eval(score=1.0, nodes=1)
    elif result == board.DRAW:
        return Eval(score=0.0, nodes=1)
    elif result == board.O_WIN:
        return Eval(score=-1.0, nodes=1)
    
    moves = board.get_legal_moves()
    evals = [evaluate(board.get_successor(m)) 
                   for m in moves]
    if board.to_move == board.PLAYER_O:
        return min_agg(evals)
    else:
        return max_agg(evals)
    


