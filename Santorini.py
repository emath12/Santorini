# singleton class
# state / mementon
# template 
# command 

class BoardSquare:

    def __init__(self, piece=None, has_worker=False):
        self.piece = piece
        self.has_worker = has_worker

    def __str__(self):
        if self.piece:
            return str(self.piece)
        else:
            return "0 "
    
    def __repr__(self):
        if self.piece:
            return str(self.piece)
        else:
            return "0 "
    
class GamePiece:
    def __init__(self, label, owner) -> None:
        self.label = label
        self.owner = owner

    def __str__(self):
        return self.label
    
class Worker(GamePiece):

    def __init__(self, label):
        super().__init__(label=label)

class Block(GamePiece):
    
    def __init__(self):
        super().__init__(label="1")
        self.height = 1
        
    def build_level(self):
        if self.height < 3:
            self.height += 1 
    
class Santorini:

    instance_count = 0

    def __init__(self): 

        if self.instance_count > 0:
            print("game is already in progress!")
            return 
        
        self.board = [
            [BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare()],
            [BoardSquare(), BoardSquare(piece=Worker(label="0Y")), BoardSquare(), BoardSquare(piece=Worker(label="0B")), BoardSquare()],
            [BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare()],
            [BoardSquare(), BoardSquare(piece=Worker(label="0A")), BoardSquare(), BoardSquare(piece=Worker(label="0Z")), BoardSquare()],
            [BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare(), BoardSquare()],
        ]

    def isWinner(self):
        for row in self.board:
            for square in row:
                if isinstance(square.piece, Block):
                    if square.piece.height == 3:
                        return [True, square.piece.owner]
                    
        return [False, 0]

    def play(self):

        while not self.isWinner()[0]:
            pass

    def __str__(self):

        string_obj = ""
         
        for row in self.board:

            string_obj += ("+--" * len(row) + "+" + "\n") 

            for square in row:

                string_obj += (f"|{square}")

            string_obj += "|"
            string_obj += "\n"
        
        string_obj += ("+--" * len(row) + "+")

        return string_obj




        
    
