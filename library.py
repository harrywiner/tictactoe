from pydantic import BaseModel

class Board():
    def __init__(self, state="", board=None):
        self.stateX = 0
        self.stateO = 0

        self.PLAYER_X = bool(0)
        self.PLAYER_O = bool(1)
        self.to_move = self.PLAYER_X
            
        self.NO_RESULT = 0
        self.DRAW = 1
        self.X_WIN = 2
        self.O_WIN = 3
        
        self.board_len=3

        self.STRING_REPRESENTATION = {
                   self. PLAYER_X: "X",
                    self.PLAYER_O: "O",
                    "empty": "-"
                }
        if state != "":
            xcount = 0
            ocount = 0
            for i, c in enumerate(state):
                if(c == self.STRING_REPRESENTATION[self.PLAYER_X]):
                    self.set_index_in_binary_string(i, self.PLAYER_X)
                    xcount += 1
                elif c == self.STRING_REPRESENTATION[self.PLAYER_O]:
                    self.set_index_in_binary_string(i, self.PLAYER_O)
                    ocount += 1
            if xcount == ocount:
                self.to_move = self.PLAYER_X
            elif xcount == ocount + 1:
                self.to_move = self.PLAYER_O
            else:
                raise "Illegal input board state"
            pass
        elif board is not None:
            self.stateO = board.stateO
            self.stateX = board.stateX
            self.to_move = board.to_move

    win_masks=[
        292,146,73,
        448,56,7,
        273,84
    ]    
    
    
    def get_legal_moves(self):
        moves = []
        state = self.stateX | self.stateO
        for i in range(self.board_len):
            for j in range(self.board_len):
                mask = 2 ** (i + j * self.board_len)
                if mask & state != mask:
                    moves.append((i, j))
        return moves
    def get_all_successors(player: bool):
        pass
    def get_successor(self, move):
        newboard = Board(board=self)
        newboard.make_move(move)
        return newboard

    def set_index_in_binary_string(self, index, player):
        if(player == self.PLAYER_X):
            self.stateX |= (1 << index)
        else:
            self.stateO |= (1 << index)
    def set_move(self, move, player):
        self.set_index_in_binary_string(move[0] + move[1] * self.board_len, self.to_move)
    def make_move(self, move: tuple[int, int]):
        self.set_move(move, self.to_move)
        self.to_move = not self.to_move
    

    def bin(self):
        return f"X's: {'{0:b}'.format(self.stateX)}, O's: {'{0:b}'.format(self.stateO)}, Filled: {'{0:b}'.format(self.stateX | self.stateO)}"
    def __str__(self):        
        output = ""
        for i in range(self.board_len):
            curr = ""
            for j in range(self.board_len):
                mask = 2 ** (j + i * self.board_len)
                if (self.stateX & mask) == mask:
                    curr += self.STRING_REPRESENTATION[self.PLAYER_X]
                elif (self.stateO & mask) == mask:
                    curr += self.STRING_REPRESENTATION[self.PLAYER_O]
                else:
                    curr += self.STRING_REPRESENTATION["empty"]
            output += curr + "\n"
        return output

    def __iter__(self):
        pass
    
    def result(self):
        if   any([w == w & self.stateO for w in self.win_masks]): return self.O_WIN
        elif any([w == w & self.stateX for w in self.win_masks]): return self.X_WIN
        elif (self.stateX | self.stateO) == 511: return self.DRAW
        else: return self.NO_RESULT
            
            
class Eval(BaseModel):
    score: int
    nodes: int
    
    def __iadd__(self, other):
        self.score += other.score
        self.nodes += other.nodes
        return self
    def __add__(self, other):
        return Eval(score=self.score + other.score, nodes=self.nodes + other.nodes)
    def average(self):
        return self.score / self.nodes

    def __str__(self):
        return f"Score: {self.score} | Nodes: {self.nodes}"
    
xwin = Board()
xwin.make_move((1,1))
xwin.make_move((0,0))
xwin.make_move((1,0))
xwin.make_move((0,1))
xwin.make_move((1,2))

assert(xwin.result() == xwin.X_WIN)
xwin = Board()
xwin.make_move((1,1))
xwin.make_move((1,0))
xwin.make_move((0,0))
xwin.make_move((0,1))
xwin.make_move((2,2))
assert(xwin.result() == xwin.X_WIN)

no_result = Board()
assert(no_result.result() == no_result.NO_RESULT)


in_test = Board(state="XX-OOX--O-")

in_test = Board(state="-OX-XOOX-")