from constants import TEXT_DIR_TO_NUM
from GameActions import Move

class GamePiece:
    def __init__(self, label, owner, coords, board) -> None:
        self.label = label
        self.owner = owner
        self.coords = coords
        self.board = board

    def __str__(self):
        return self.label
    
    def __repr__(self):
        return self.label
    
class Worker(GamePiece):

    def __init__(self, label, owner, coords, board):
        super().__init__(label=label, owner=owner, coords=coords, board=board)

    def can_move(self):
        
        return self.generate_valid_moves(self.coords) != []

    def generate_valid_moves(self, coords):
        valid_moves : [Move]  = []

        valid_worker_movements = self.board.generate_valid_move_dirs(coords)
        for vw in valid_worker_movements:
            valid_worker_builds = self.board.generate_valid_build_dirs([sum(x) for x in zip(coords, TEXT_DIR_TO_NUM[vw])])
            for vb in valid_worker_builds:
                valid_moves.append(Move(self, vw, vb))

        return valid_moves
    
    def __eq__(self, value : str) -> bool:
        if str(value) == str(self.label):
            return True
        else:
            return False

    # def generate_valid_moves(self) -> [Move]:
        

    #     d_combos = combinations(valid_piece_move_dirs, 2)
    #     for move_dir, build_dir in valid_piece_move_dirs:
    #         valid_piece_moves.append(Move(worker=self, move_dir=move_dir, build_dir=build_dir))

    #     return valid_piece_moves

    # def generate_valid_builds(self, )
