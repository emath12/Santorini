# state / mementon - undo/redo
# strategy - type of player 
# abstract factory, composite (?)

from GamePiece import Worker, Block
from GameAction import QueryPlayer, PrintBoard, Turn, Move

class Player:

    def __init__(self, board, color, workers) -> None:
        self.board = board
        self.color = color
        self.workers = workers

    def can_move():
        pass

class BoardSquare:

    def __init__(self, piece=None):
        self.piece = piece

    def __str__(self):
        if self.piece:
            return str(self.piece)
        else:
            return "0 "
    
    def __repr__(self):
        if self.piece:
            return str(self.piece)
        else:
            return "0 "
        
class Board:

    def __init__(self) -> None:

        self.board = [
            [BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare()],
            [BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare()],
            [BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare()],
            [BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare()],
            [BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare()],
        ]

        self.row_ind = 0
        self.col_ind = 0
        self.max_row = len(self.board)
        self.max_col = len(self.board[0])

        self.board[1][3].piece = Worker(label="0B", owner="blue", coords=[1, 3], board=self.board)
        self.board[1][1].piece = Worker(label="0Y", owner='blue', coords=[1, 1], board=self.board)
        self.board[3][1].piece = Worker(label="0A", owner="white", coords=[3, 1], board=self.board)
        self.board[3][3].piece = Worker(label="0Z", owner="white", coords=[3, 3], board=self.board)

    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.row_ind >= self.max_row:
            raise StopIteration
        
        value = self.board[self.row_ind][self.col_ind]
        self.col_ind += 1

        if self.col_ind >= self.max_col:
            self.col_ind = 0
            self.row_ind += 1

        return value

    def __repr__(self) -> str:
        
        string_obj = ""
         
        for row in self.board:

            string_obj += ("+--" * len(row) + "+" + "\n") 

            for square in row:

                string_obj += (f"|{square}")

            string_obj += "|"
            string_obj += "\n"
        
        string_obj += ("+--" * len(row) + "+")

        return string_obj

    def __str__(self) -> str:
        return repr(self)
    
    def __getitem__(self, inds):
        row, col = inds
        return self.board[row][col]

class Santorini:

    def __init__(self): 
        self.board : Board = Board()
        self.current_turn : Turn = None

    def isWinner(self):
        for ele in self.board:
            if isinstance(ele.piece, Block):
                if ele.piece.height == 3:
                    return [True, ele.piece.owner]
                    
        return [False, 0]
    
    def print_round(self):
        print(self.current_turn)
        print(self.board)

    def play(self):
        self.current_turn = Turn(player=1)
        self.print_round()

        while not self.isWinner()[0]:
            
            moved_worker = input("Select a worker to move \n")
            move_dir = input("Select a direction to move (n, ne, e, se, s, sw, w, nw) \n")
            build_dir = input("Select a direction to build (n, ne, e, se, s, sw, w, nw) \n")
            
            print(Move(moved_worker, move_dir, build_dir))

            if self.current_turn.player == 1:
                self.current_turn = Turn(player=2)
            else:
                self.current_turn = Turn(player=1)

            self.print_round()

       
    
