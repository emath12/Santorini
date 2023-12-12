from constants import TEXT_DIR_TO_NUM
from GameActions import Move

    
class Worker:

    def __init__(self, label, owner, coords, board=None):
        self.board=board
        self.label = label
        self.owner = owner
        self.coords = coords

    def can_move(self):
        """
        Checks if the given worker can move, by checking if it
        has any valid moves.
        """
        
        return self.generate_valid_moves() != []

    def generate_valid_moves(self):
        """
        Generates the valid moves a worker can make. Returns an array of 
        move objects.
        """
        valid_moves : [Move]  = []

        valid_worker_movements = self.board.generate_valid_move_dirs(self.coords)

        for vw in valid_worker_movements:
            valid_worker_builds = self.board.generate_valid_build_dirs([sum(x) for x in zip(self.coords, TEXT_DIR_TO_NUM[vw])])
            for vb in valid_worker_builds:
                added_move = Move(self, vw, vb)
                added_move.get_move_score()
                valid_moves.append(added_move)

        return valid_moves
    
    def __eq__(self, value : str) -> bool:
        if str(value) == str(self.label):
            return True
        else:
            return False
        
    def __deepcopy__(self, memo):
        return Worker(self.label, self.owner, self.coords, board=None)
    
    def __str__(self):
        return self.label
    
    def __repr__(self):
        return self.label

    # def generate_valid_moves(self) -> [Move]:
        

    #     d_combos = combinations(valid_piece_move_dirs, 2)
    #     for move_dir, build_dir in valid_piece_move_dirs:
    #         valid_piece_moves.append(Move(worker=self, move_dir=move_dir, build_dir=build_dir))

    #     return valid_piece_moves

    # def generate_valid_builds(self, )
