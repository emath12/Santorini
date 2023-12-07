# state / mementon - undo/redo
# strategy - type of player 
# iterator - board?
# decorator - somewhere :

# abstract factory, composite (?)

from GameComponent import Board, Direction, Worker, DIRECTIONS
from GameActions import Turn, Move
from Player import Player 
from exceptions import InvalidWorker, NotYourWorker, InvalidDirection, InvalidMovementDirection, InvalidBuildDirection
from GamePiece import GamePiece
from constants import TEXT_DIR_TO_NUM

# strategy pattern, implement the same methods
class SantoriniRandom:
    pass

class SantoriniHeurisitic:
    pass

class Santorini:

    def __init__(self): 
        self.board : Board = Board()
        self.current_turn : Turn = None
        self.current_player : Player = None

        self.worker_Y = self.board[1, 1].piece
        self.worker_B = self.board[1, 3].piece
        self.worker_A = self.board[3, 1].piece
        self.worker_Z = self.board[3, 3].piece 

        self.players = [
            Player(board=self.board, color="blue", workers=[self.worker_Y, self.worker_Z]),
            Player(board=self.board, color="white", workers=[self.worker_A, self.worker_B])
        ]

    def isWinner(self):
        for ele in self.board:
            if isinstance(ele, GamePiece) and ele.piece.height == 3:
                    return [True, ele.piece.owner]
                    
        return [False, None]
    
    def print_round(self):
        print(self.current_turn)
        print(self.board)

    def play(self):
        self.current_turn = Turn(player=self.players[0])
        self.print_round()
        self.current_player = self.players[0]
        invalid_worker = True
        invalid_move_dir = True
        invalid_build_dir = True
        
        while not self.isWinner()[0]:
            
            while invalid_worker:
                try:
                    inputted_worker : Worker = input("Select a worker to move \n")

                    if inputted_worker != "A" and inputted_worker != "B" and inputted_worker != "Y" and inputted_worker != "Z":
                        raise InvalidWorker  

                    if not inputted_worker == self.current_player.workers[0].label and not inputted_worker == self.current_player.workers[1].label :
                        raise NotYourWorker
                    
                    invalid_worker = False
                    
                    if inputted_worker == "A":
                        inputted_worker = self.worker_A
                    elif inputted_worker == "B":
                        inputted_worker = self.worker_B
                    elif inputted_worker == "Y":
                        inputted_worker = self.worker_Y
                    else:
                        inputted_worker = self.worker_Z

                except InvalidWorker:
                    print("Not a valid worker")
                except NotYourWorker:
                    print("That is not your worker")
            
            valid_move_directions = self.board.generate_valid_move_dirs(inputted_worker.coords)

            while invalid_move_dir:
                try:
                    move_dir = input("Select a direction to move (n, ne, e, se, s, sw, w, nw) \n")

                    if move_dir not in DIRECTIONS:
                        raise InvalidDirection
                    if move_dir not in valid_move_directions:
                        raise InvalidMovementDirection
                    
                    invalid_move_dir = False
                
                except InvalidDirection:
                    print("Not a valid direction")
                except InvalidMovementDirection:
                    print(f"Cannot move {move_dir}")

            while invalid_build_dir:

                try:

                    build_dir = input("Select a direction to build (n, ne, e, se, s, sw, w, nw) \n")
                    valid_build_directions = self.board.generate_valid_build_dirs([sum(x) for x in zip(inputted_worker.coords, TEXT_DIR_TO_NUM[build_dir])])

                    if build_dir not in DIRECTIONS:
                        raise InvalidDirection
                    if build_dir not in valid_build_directions:
                        raise InvalidMovementDirection
                    
                    invalid_build_dir = False
                    
                except InvalidDirection:
                    print("Not a valid direction")
                except InvalidBuildDirection:
                    print(f"Cannot build {build_dir}")
                
            made_move = Move(inputted_worker, move_dir, build_dir)

            self.board.move_worker(inputted_worker, num_move_dir=made_move.num_move_dir)
            self.board.build(inputted_worker, build_dir=made_move.num_build_dir)

            if self.current_player.color == "blue":
                self.current_turn = Turn(player=self.players[1])
                self.current_player = self.players[1]
            else:
                self.current_turn = Turn(player=self.players[0])
                self.current_player = self.players[0]

            self.print_round()
            invalid_build_dir = True
            invalid_move_dir = True
            invalid_worker = True
            

       
    
