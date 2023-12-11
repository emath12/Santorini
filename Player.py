from GamePiece import Worker
from GameComponent import Board
from GameActions import Move
from exceptions import *
from constants import *
import random
import copy
class PlayerType:
    HUMAN = 1
    RANDOM = 2
    HEURISTIC = 3

class Player:

    def __init__(self, board, color, workers) -> None:
        self.board : Board = board
        self.color : str = color
        self.workers : [Worker] = workers
        self.score = None

    def check_can_move(self):
        
        for worker in self.workers:
            if worker.can_move():
                return True
        
        return False
    
    def get_my_score(self):
        snapshot_move = Move(self.workers[0], "-", "-")
        snapshot_move_score = snapshot_move.get_move_score()
        self.score = snapshot_move_score
        return snapshot_move_score
    
    def make_move(self) -> Move:

        invalid_worker = True
        invalid_move_dir = True
        invalid_build_dir = True

        while invalid_worker:
            try:
                inputted_worker : Worker = input("Select a worker to move\n")

                if inputted_worker != "A" and inputted_worker != "B" and inputted_worker != "Y" and inputted_worker != "Z":
                    raise InvalidWorker  

                if not inputted_worker == self.workers[0].label and not inputted_worker == self.workers[1].label :
                    raise NotYourWorker
                
                if inputted_worker == self.workers[0].label:
                    inputted_worker = self.workers[0]
                elif inputted_worker == self.workers[1].label:
                    inputted_worker = self.workers[1]
                   
                if not inputted_worker.can_move():
                    raise WorkerCannotMove
                
                invalid_worker = False

                copy_of_inputted_worker = copy.deepcopy(inputted_worker)
                copy_of_inputted_worker.board = self.board

                valid_move_directions = self.board.generate_valid_move_dirs(inputted_worker.coords)

            except InvalidWorker:
                print("Not a valid worker")
            except NotYourWorker:
                print("That is not your worker")
            except WorkerCannotMove:
                print("That worker cannot move")
            
        while invalid_move_dir:
            try:
                move_dir = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")

                if move_dir not in DIRECTIONS:
                    raise InvalidDirection
                if move_dir not in valid_move_directions:
                    raise InvalidMovementDirection
                
                self.board.move_worker(inputted_worker, move_dir)
                
                invalid_move_dir = False
            
            except InvalidDirection:
                print("Not a valid direction")
            except InvalidMovementDirection:
                print(f"Cannot move {move_dir}")

        while invalid_build_dir:

            try:

                build_dir = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
                
                valid_build_directions = self.board.generate_valid_build_dirs(inputted_worker.coords)

                if build_dir not in DIRECTIONS:
                    raise InvalidDirection
                if build_dir not in valid_build_directions:
                    raise InvalidBuildDirection
                
                self.board.build(inputted_worker, build_dir)

                invalid_build_dir = False
                
            except InvalidDirection:
                print("Not a valid direction")
            except InvalidBuildDirection:
                print(f"Cannot build {build_dir}")
        
        made_move =  Move(copy_of_inputted_worker, move_dir, build_dir)
        made_move.get_move_score()
        return made_move

    def __str__(self):

        return f"""
        {self.color}
        {self.workers}
        """
    
    def __deepcopy__(self, memo):
        return Player(board=None, color=self.color, workers=None)

class HeurisiticPlayer(Player):
    def __init__(self, board, color, workers) -> None:
        super().__init__(board, color, workers)

    def make_move(self) -> Move:
        
        valid_moves = []

        for worker in self.workers:
            valid_moves += worker.generate_valid_moves()
        
        best_moves = sorted(valid_moves, key=lambda move : move.move_score.get_move_score(), reverse=True)
        
        made_move = best_moves[0]

        self.board.move_worker(made_move.worker, made_move.move_dir)
        self.board.build(made_move.worker, made_move.build_dir)

        return made_move

class RandomPlayer(Player):

    def __init__(self, board, color, workers) -> None:
        super().__init__(board, color, workers)
    
    def make_move(self) -> Move:

        selected_index, selected_worker = random.choice(list(enumerate(self.workers)))
        
        valid_moves = selected_worker.generate_valid_moves()

        if not valid_moves:
            if selected_index == 0:
                valid_moves = self.workers[1].generate_valid_moves()
            else:
                valid_moves = self.workers[0].generate_valid_moves()

        
        return random.choice(valid_moves)
    