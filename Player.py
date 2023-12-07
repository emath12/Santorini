from GamePiece import Worker
from GameComponent import Board
from GameActions import Move


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
    
    def move_worker(self, worker : Worker, move : Move):

        worker.coords += move.num_move_dir
        self.board.move_worker()

    def __str__(self):

        return f"""
        {self.color}
        {self.workers}
        """


