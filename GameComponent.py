from GamePiece import Worker, GamePiece
from constants import COLUMN_COUNT, ROW_COUNT, TEXT_DIR_TO_NUM, MAX_HEIGHT
from enum import Enum
from GameActions import Move
import copy

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    WEST = "w"
    EAST = "e"
    NORTH_WEST = "nw"
    NORTH_EAST = "ne"
    SOUTH_EAST = "se"
    SOUTH_WEST = "sw"

class BoardSquare:

    def __init__(self, piece=None, height=0):
        self.piece : Worker = piece
        self.height = height

    def build_level(self):
        if self.height < 3:
            self.height += 1 

    def __str__(self):
        if self.piece:
            return str(self.height) + str(self.piece)
        else:
            return f"{self.height} "
    
    def __repr__(self):
        if self.piece:
            return str(self.height) + str(self.piece)
        else:
            return f"{self.height} "
    
    def __deepcopy__(self, memo):

        if self.piece:

            return BoardSquare(
                    piece=copy.deepcopy(self.piece), 
                    height=self.height
            )

        else:

            return BoardSquare(
                piece=None,
                height=self.height
            )
    
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

        self.worker_Y = Worker(label="Y", owner='blue', coords=[1, 1], board=self)
        self.worker_B = Worker(label="B", owner="blue", coords=[1, 3], board=self)
        self.worker_A = Worker(label="A", owner="white", coords=[3, 1], board=self)
        self.worker_Z = Worker(label="Z", owner="white", coords=[3, 3], board=self)

        self.board[1][3].piece = self.worker_B
        self.board[1][1].piece = self.worker_Y
        self.board[3][1].piece = self.worker_A
        self.board[3][3].piece = self.worker_Z 


    def move_worker(self, worker, d):

        if d == "-":
            return
        
        old_x, old_y = worker.coords 

        x_move, y_move = TEXT_DIR_TO_NUM[d]

        self.board[old_x][old_y].piece = None
        self.board[old_x + x_move][old_y + y_move].piece = worker

        worker.coords = [old_x + x_move, old_y + y_move] 

        return [old_x + x_move, old_y + y_move] 
    
    def build(self, worker, d):
        worker_x, worker_y = worker.coords
        x_build, y_build = TEXT_DIR_TO_NUM[d]

        if d == "-":
            return

        self.board[worker_x + x_build][worker_y + y_build].build_level()

    def generate_valid_move_dirs(self, coords):

        r, c = coords
        valid_piece_move_dirs = []

        directions = [(1, 0, "s"), (-1, 0, "n"), (0, -1, "w"), (0, 1, "e")]
        diagonals = [(-1, 1, "ne"), (-1, -1, "nw"), (1, -1, "sw"), (1, 1, "se")]

        for dr, dc, dir_str in directions + diagonals:
            
            new_r, new_c = r + dr, c + dc

            if (
                0 <= new_r < ROW_COUNT
                and 0 <= new_c < COLUMN_COUNT
                and self.board[new_r][new_c].height < MAX_HEIGHT
                and self.board[r][c].height - self.board[new_r][new_c].height <= 1
                and not self.board[new_r][new_c].piece
            ):
                
                valid_piece_move_dirs.append(dir_str)

        return valid_piece_move_dirs

    def generate_valid_build_dirs(self, coords):

        r, c = coords
        valid_piece_build_dirs = []

        directions = [(1, 0, "s"), (-1, 0, "n"), (0, 1, "e"), (0, -1, "w")]
        diagonals = [(-1, 1, "ne"), (-1, -1, "nw"), (1, -1, "sw"), (1, 1, "se")]

        for dr, dc, dir_str in directions + diagonals:
            new_r, new_c = r + dr, c + dc

            if (0 <= new_r < ROW_COUNT and 
                0 <= new_c < COLUMN_COUNT and 
                self.board[new_r][new_c].piece == None and
                self.board[new_r][new_c].height < MAX_HEIGHT
                ):
                valid_piece_build_dirs.append(dir_str)

        return valid_piece_build_dirs
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.row_ind >= self.max_row:
            raise StopIteration
        
        value = self.board[self.row_ind][self.col_ind]
        index = (self.row_ind, self.col_ind)
        self.col_ind += 1

        if self.col_ind >= self.max_col:
            self.col_ind = 0
            self.row_ind += 1

        return index, value

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

    def __setitem__(self, indices, value):
        row, col = indices
        self.board[row][col] = value

    def __deepcopy__(self, memo):

        new_board = Board()

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                new_board[r, c] = copy.deepcopy(self.board[r][c], memo)
                if self.board[r][c].piece:
                    new_board[r, c].piece.board = new_board

        

            # if self.board[row][col].piece:
            #     new_board[row, col].piece = copy.deepcopy(self.board[row][col].piece)
            #     new_board[row, col].piece.coords = self.board[row][col].piece.coords

            # new_board[row, col].height = self.board[row][col].height

        new_board.row_ind = self.row_ind
        new_board.col_ind = self.col_ind
        new_board.max_row = self.max_row
        new_board.max_col = self.max_col

        new_board.worker_B = copy.deepcopy(self.worker_B)
        new_board.worker_Y = copy.deepcopy(self.worker_Y)
        new_board.worker_A = copy.deepcopy(self.worker_A)
        new_board.worker_Z = copy.deepcopy(self.worker_Z)

        return new_board