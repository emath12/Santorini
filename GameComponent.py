from GamePiece import Worker, GamePiece
from constants import COLUMN_COUNT, ROW_COUNT, TEXT_DIR_TO_NUM, MAX_HEIGHT
from enum import Enum

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    WEST = "w"
    EAST = "e"
    NORTH_WEST = "nw"
    NORTH_EAST = "ne"
    SOUTH_EAST = "se"
    SOUTH_WEST = "sw"

DIRECTIONS = ["ne", "n", "e", "se", "sw", "s", "nw", "w"]


class BoardSquare:

    def __init__(self, piece=None):
        self.piece : GamePiece = piece
        self.height = 0 

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

        self.board[1][3].piece = Worker(label="B", owner="blue", coords=[1, 3], board=self)
        self.board[1][1].piece = Worker(label="Y", owner='blue', coords=[1, 1], board=self)
        self.board[3][1].piece = Worker(label="A", owner="white", coords=[3, 1], board=self)
        self.board[3][3].piece = Worker(label="Z", owner="white", coords=[3, 3], board=self)

    def move_worker(self, worker : Worker, num_move_dir):
        old_x, old_y = worker.coords 

        x_move, y_move = num_move_dir

        self.board[old_x][old_y].piece = None
        self.board[old_x + x_move][old_y + y_move].piece = worker

        worker.coords = [old_x + x_move, old_y + y_move] 

    def build(self, worker : Worker, build_dir):
        worker_x, worker_y = worker.coords
        x_build, y_build = build_dir

        self.board[worker_x + x_build][worker_y + y_build].build_level()

    def generate_valid_move_dirs(self, coords):

        r, c = coords

        valid_piece_move_dirs : [Direction] = []

        # generate the valid piece moves
        if (r + 1 < ROW_COUNT and 
            self.board[r + 1][c].height < MAX_HEIGHT and 
            abs(self.board[r + 1][c].height - self.board[r][c].height) < 1 and
            not self.board[r + 1][c].piece 
        ):
            valid_piece_move_dirs.append("s")

        if (r - 1 >= 0 and 
            self.board[r - 1][c].height < MAX_HEIGHT and 
            abs(self.board[r - 1][c].height - self.board[r][c].height) < 1 and
            not self.board[r - 1][c].piece 
        ):
            valid_piece_move_dirs.append("n")
        
        if (c - 1 >= 0 and 
            self.board[r][c - 1].height < MAX_HEIGHT and 
            abs(self.board[r][c - 1].height - self.board[r][c].height) < 1 and
            not self.board[r][c - 1].piece 
        ):
            valid_piece_move_dirs.append("w")

        if (c + 1 < COLUMN_COUNT and 
            self.board[r][c + 1].height < MAX_HEIGHT and 
            abs(self.board[r][c + 1].height - self.board[r][c].height) < 1 and
            not self.board[r][c + 1].piece 
        ):
            valid_piece_move_dirs.append("e")

        if "n" in valid_piece_move_dirs and "e" in valid_piece_move_dirs and abs(self.board[r + 1][c + 1].height - self.board[r][c].height) < 1:
            valid_piece_move_dirs.append("ne")
        if "n" in valid_piece_move_dirs and "w" in valid_piece_move_dirs and abs(self.board[r - 1][c + 1].height - self.board[r][c].height) < 1:
            valid_piece_move_dirs.append("nw")
        if "s" in valid_piece_move_dirs and "w" in valid_piece_move_dirs and abs(self.board[r - 1][c - 1].height - self.board[r][c].height) < 1:
            valid_piece_move_dirs.append("sw")
        if "s" in valid_piece_move_dirs and "e" in valid_piece_move_dirs and abs(self.board[r + 1][c - 1].height - self.board[r][c].height) < 1:
            valid_piece_move_dirs.append("se")

        return valid_piece_move_dirs

    def generate_valid_build_dirs(self, coords):

        r, c = coords


        valid_piece_build_dirs : [Direction] = []

        if r + 1 < COLUMN_COUNT :
            valid_piece_build_dirs.append("s")
        if r - 1 >= 0  :
            valid_piece_build_dirs.append("n")
        if c + 1 < COLUMN_COUNT:
            valid_piece_build_dirs.append("e")
        if c - 1 >= 0 :
            valid_piece_build_dirs.append("w")

        if "n" in valid_piece_build_dirs and "e" in valid_piece_build_dirs:
            valid_piece_build_dirs.append("ne")
        if "n" in valid_piece_build_dirs and "w" in valid_piece_build_dirs:
            valid_piece_build_dirs.append("nw")
        if "s" in valid_piece_build_dirs and "w" in valid_piece_build_dirs:
            valid_piece_build_dirs.append("sw")
        if "s" in valid_piece_build_dirs and "e" in valid_piece_build_dirs:
            valid_piece_build_dirs.append("se")

        return valid_piece_build_dirs
        
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
