from GamePiece import Worker
from GameComponent import Board
from GameActions import Move
from exceptions import *
from constants import *

class PlayerType:
    HUMAN = 1
    RANDOM = 2
    HEURISTIC = 3

class Player:

    def __init__(self, board, color, workers) -> None:
        self.board : Board = board
        self.color : str = color
        self.workers : [Worker] = workers

    def can_move():
        
        for worker in worker:
            if worker.can_move():
                return True
        
        return False
    
    def make_move(self) -> Move:

        invalid_worker = True
        invalid_move_dir = True
        invalid_build_dir = True

        while invalid_worker:
            try:
                inputted_worker : Worker = input("Select a worker to move \n")

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

    def __str__(self):

        return f"""
        {self.color}
        {self.workers}
        """
    
class HeurisiticPlayer(Player):
    pass 

class RandomPlayer(Player):
    pass


