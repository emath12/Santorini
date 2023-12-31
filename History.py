import copy 

class SantoriniState:

    def __init__(
            self, 
            board, 
            current_turn, 
            current_color,
            current_player, 
            players,
            worker_Y,
            worker_Z,
            worker_A,
            worker_B
        ) -> None:
            
            self.new_board = copy.deepcopy(board)
            
            self.current_turn : int = current_turn

            self.players = copy.deepcopy(players)

            self.worker_Y = copy.deepcopy(worker_Y)
            self.worker_Z = copy.deepcopy(worker_Z)
            self.worker_A = copy.deepcopy(worker_A)
            self.worker_B = copy.deepcopy(worker_B)

            players[0].workers = [self.worker_A, self.worker_B]
            players[1].workers = [self.worker_Y, self.worker_Z]
            players[0].board = self.new_board
            players[1].board = self.new_board

            if current_player.color == "blue":
                self.current_player = players[1]
            else:
                self.current_player = players[0]

            self.worker_Y.board = self.new_board
            self.worker_A.board = self.new_board
            self.worker_B.board = self.new_board
            self.worker_Z.board = self.new_board
            self.current_color = current_color

class History:

    def __init__(self) -> None:
        self.history = []
        self.redos = []

    def pop_redos(self):
        """
        Gets the most recent undo
        """
        
        if not self.redos:
            return None 

        return self.redos.pop()
    
    def push_redos(self, san):
        """
        Adds an undo to the redo stack
        """

        self.redos.append(san)

    def pop_history(self):
        """
        Pops the most recent action off the stack and returns a
        SantoriniState object.
        """

        if not self.history:
            return None

        return self.history.pop()
    
    def push_history(self, san):
        """
        Adds a state of the game to the stack.
        """

        self.history.append(san)