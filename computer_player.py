from library import Board, Eval

def get_best_move(board: Board) -> tuple((int, int)):
    moves = board.get_legal_moves()
    best_move = (0, 0)
    best_eval = 0.0
    for m in moves:
        candidate = board.get_successor(m)
        E = evaluate(candidate)
        if E.average() > best_eval:
            best_move = m
            best_eval = E.score
    return best_move

def evaluate(board: Board) -> float:
    result = board.result()
    if result == board.X_WIN:
        return Eval(score=1.0, nodes=1)
    elif result == board.O_WIN:
        return Eval(score=0.0, nodes=1)
    elif result == board.O_WIN:
        return Eval(score=-1.0, nodes=1)
    
    moves = board.get_legal_moves()
    evals = [evaluate(board.get_successor(m)) 
                   for m in moves]
    total = evals[0]
    for i in range(1, len(evals)):
        total += evals[i]
    return total

if __name__ == "__main__":
    eval_test_1 = Board(state="XX-OOX--O-")
    print(get_best_move(eval_test_1))
    eval_test_2 = Board(state="-OX-XOOX-")
    print(get_best_move(eval_test_2))
