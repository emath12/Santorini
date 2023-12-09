# state / mementon - undo/redo
# strategy - type of Santontoi Game
# decorator - somewhere :
# template - execute play + diff games imp it


# abstract factory, composite (?)

from GameComponent import Board, BoardSquare, Direction, Worker
from GameActions import Turn, Move
from Player import Player, HeurisiticPlayer, RandomPlayer
from exceptions import InvalidWorker, NotYourWorker, InvalidDirection, InvalidMovementDirection, InvalidBuildDirection, WorkerCannotMove
from constants import *
from Player import PlayerType

class Santorini:

    def __init__(self, player_1_type, player_2_type, undo_redo_enabled=False, enabled_display_score=False): 
        self.board : Board = Board()
        self.current_turn : Turn = None
        self.current_player : Player = None

        self.worker_Y = self.board[1, 1].piece
        self.worker_B = self.board[1, 3].piece
        self.worker_A = self.board[3, 1].piece
        self.worker_Z = self.board[3, 3].piece 

        self.winner = None
        self.undo_redo_enabled = undo_redo_enabled
        self.enabled_display_score = enabled_display_score

        self.players = []

        if player_1_type == PlayerType.HUMAN:
            self.players.append(Player(board=self.board, color="white", workers=[self.worker_A, self.worker_B]))
        elif player_1_type == PlayerType.RANDOM:
            self.players.append(RandomPlayer(board=self.board, color="white", workers=[self.worker_A, self.worker_B]))
        else:
            self.players.append(HeurisiticPlayer(board=self.board, color="white", workers=[self.worker_A, self.worker_B]))

        if player_2_type == PlayerType.HUMAN:
            self.players.append(Player(board=self.board, color="blue", workers=[self.worker_Y, self.worker_Z]))
        elif player_2_type == PlayerType.RANDOM:
            self.players.append(RandomPlayer(board=self.board, color="blue", workers=[self.worker_Y, self.worker_Z]))
        else:
            self.players.append(HeurisiticPlayer(board=self.board, color="blue", workers=[self.worker_Y, self.worker_Z]))

      

        
                            
    def isWinner(self):

        if not any(worker.can_move() for worker in self.current_player.workers):
            return [True, None]

        for ele in self.board:
            if isinstance(ele, BoardSquare) and ele.height == 3:
                    return [True, ele.piece.owner]
        
        return [False, None]
    
    def print_round(self):
        print(self.current_turn)
        print(self.board)

    def make_move(self) -> Move:

        invalid_worker = True
        invalid_move_dir = True
        invalid_build_dir = True

        while invalid_worker:
            try:
                inputted_worker : Worker = input("Select a worker to move \n")

                if inputted_worker != "A" and inputted_worker != "B" and inputted_worker != "Y" and inputted_worker != "Z":
                    raise InvalidWorker  

                if not inputted_worker == self.current_player.workers[0].label and not inputted_worker == self.current_player.workers[1].label :
                    raise NotYourWorker
                
                if inputted_worker == "A":
                    inputted_worker = self.worker_A
                elif inputted_worker == "B":
                    inputted_worker = self.worker_B
                elif inputted_worker == "Y":
                    inputted_worker = self.worker_Y
                else:
                    inputted_worker = self.worker_Z
                
                if not inputted_worker.can_move():
                    raise WorkerCannotMove
                
                invalid_worker = False
            
            except InvalidWorker:
                print("Not a valid worker")
            except NotYourWorker:
                print("That is not your worker")
            except WorkerCannotMove:
                print("That worker cannot move")
            
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
                
                print([sum(x) for x in zip(inputted_worker.coords, TEXT_DIR_TO_NUM[build_dir])])
                valid_build_directions = self.board.generate_valid_build_dirs([sum(x) for x in zip(inputted_worker.coords, TEXT_DIR_TO_NUM[move_dir])])

                if build_dir not in DIRECTIONS:
                    raise InvalidDirection
                if build_dir not in valid_build_directions:
                    raise InvalidBuildDirection
                
                invalid_build_dir = False
                
            except InvalidDirection:
                print("Not a valid direction")
            except InvalidBuildDirection:
                print(f"Cannot build {build_dir}")
                
        return Move(inputted_worker, move_dir, build_dir)

    def play(self):
        self.current_turn = Turn(player=self.players[0])
        self.print_round()
        self.current_player = self.players[0]
        
        while not self.isWinner()[0]:
            
            made_move = self.current_player.make_move()
            
            self.board.move_worker(made_move)
            self.board.build(made_move)

            if self.current_player.color == "blue":
                self.current_turn = Turn(player=self.players[1])
                self.current_player = self.players[1]
            else:
                self.current_turn = Turn(player=self.players[0])
                self.current_player = self.players[0]

            self.print_round()
            
# strategy pattern, implement the same methods
class SantoriniRandom(Santorini):
    pass

class SantoriniHeurisitic(Santorini):
    pass
