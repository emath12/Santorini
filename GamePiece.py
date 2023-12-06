class GamePiece:
    def __init__(self, label, owner, coords, board) -> None:
        self.label = label
        self.owner = owner
        self.coords = coords
        self.board = board

    def __str__(self):
        return self.label
    
class Worker(GamePiece):

    def __init__(self, label, owner, coords, board):
        super().__init__(label=label, owner=owner, coords=coords, board=board)

class Block(GamePiece):
    
    def __init__(self, owner, coords, board):
        super().__init__(label="1", owner=owner, coords=coords, board=board)
        self.height = 1
        
    def build_level(self):
        if self.height < 3:
            self.height += 1 