from computer_player import get_best_move
from library import Board
import re
import sys
from rich import print

COMPUTER = 0
HUMAN = 1

def run_computer_tests():
    tests = [{
        "state": "XX-OOX--O-",
        "eval": 1.0,
        "move": (2,0)
    },{
        "state": "-OX-XOOX-",
        "eval": 0.0,
        "move": None
    },]
    
    # eval_test_1 = Board(state="XX-OOX--O-")
    # move_1, eval_1 = get_best_move(eval_test_1)
    # print(f"Best Move: {move_1}, best eval: {eval_1}")
    # assert (move_1 == (2,0) and eval_1 == 1.0)
    # print("[bold green]Test 1 passed!")
    # eval_test_2 = Board(state="-OX-XOOX-")
    # move_2, eval_2 = get_best_move(eval_test_2)
    # print(f"Best Move: {move_2}, best eval: {eval_2}")
    # assert (eval_2 == 0.0)
    # print("[bold green]Test 2 passed!")
    
    for idx, t in enumerate(tests):
        res = run_test(t["state"], t["eval"], t["move"], debug=True, idx=idx)
        if res:
            print(f"[bold green]Test {idx} passed!")
        else:
            print(f"[bold red]Test {idx} failed!")

def run_test(state:str, eval_target:int, move_target=None, debug=False, idx=-1):
    eval_test = Board(state=state)
    move_real, eval_real = get_best_move(eval_test)
    if debug:
        print(f"Det. Move: {move_real}, Det. eval: {eval_real.score}")
        print(f"Target Move: {move_target}, Target Eval: {eval_target}")
        print(f"Found in {eval_real.nodes} leaves")
    passed = eval_target == eval_real.score and (not move_target or move_target == move_real)
    return passed

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "comptest":
            run_computer_tests()
    else:
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