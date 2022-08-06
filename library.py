

class Board(BaseModel):
    stateX: int
    stateO: int
    
    PLAYER_X = bool(0)
    PLAYER_O = bool(1)
    
    NO_RESULT = 0
    DRAW = 1
    X_WIN = 2
    O_WIN = 3
    
    board_len=3
    
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
    def make_move(self, move: tuple[int, int], player: bool):
        if player == PLAYER_X:
            self.stateX |= (1 << (move[0] + move[1] * self.board_len))
        elif player == PLAYER_O:
            self.stateO |= (1 << (move[0] + move[1] * self.board_len))
        pass
    def __str__(self):
        return f"X's: {'{0:b}'.format(self.stateX)}, O's: {'{0:b}'.format(self.stateO)}, Filled: {'{0:b}'.format(self.stateX | self.stateO)}"
    
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
    
    def __str__(self):
        return f"Score: {self.score} | Nodes: {self.nodes}"
    
xwin = Board(stateX=0, stateO=0)
xwin.make_move((1,1), PLAYER_X)
xwin.make_move((0,0), PLAYER_O)
xwin.make_move((1,0), PLAYER_X)
xwin.make_move((0,1), PLAYER_O)
xwin.make_move((1,2), PLAYER_X)
assert(xwin.result() == xwin.X_WIN)
xwin = Board(stateX=0, stateO=0)
xwin.make_move((1,1), PLAYER_X)
xwin.make_move((1,0), PLAYER_O)
xwin.make_move((0,0), PLAYER_X)
xwin.make_move((0,1), PLAYER_O)
xwin.make_move((2,2), PLAYER_X)
assert(xwin.result() == xwin.X_WIN)

no_result = Board(stateX=0, stateO=0)
assert(no_result.result() == no_result.NO_RESULT)