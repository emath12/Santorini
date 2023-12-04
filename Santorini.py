class Piece:

    def __init__(self, value="0 "):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)

class Santorini:

    def __init__(self, players: int): 
        
        self.board = [
            [Piece(), Piece(), Piece(), Piece(), Piece()],
            [Piece(), Piece("0Y"), Piece(), Piece("0B"), Piece()],
            [Piece(), Piece(), Piece(), Piece(), Piece()],
            [Piece(), Piece("OA"), Piece(), Piece("0Z"), Piece()],
            [Piece(), Piece(), Piece(), Piece(), Piece()],
        ]


    def __str__(self):

        string_obj = ""
         
        for row in self.board:

            string_obj += ("+--" * len(row) + "+" + "\n") 

            for square in row:

                string_obj += (f"|{square.value}")

            string_obj += "|"
            string_obj += "\n"
        
        string_obj += ("+--" * len(row) + "+")

        return string_obj




        
    
