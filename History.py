import copy 

class SantoriniState:

    def __init__(
            self, 
            board, 
            current_turn, 
            current_player, 
            player_1_type, 
            player_2_type,
            players,
            undo_redo_enabled,
            enabled_display_score,
            worker_Y,
            worker_Z,
            worker_A,
            worker_B
        ) -> None:
            
            self.new_board = copy.deepcopy(board)
            
            self.current_turn : int = current_turn
            self.player_1_type = player_1_type
            self.player_2_type = player_2_type
            self.undo_redo_enabled = undo_redo_enabled
            self.enabled_display_score = enabled_display_score

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

class History:

    def __init__(self) -> None:
        self.history = []
        self.redos = []

    def pop_redos(self):
        if not self.redos:
            return None 

        return self.redos.pop()
    
    def push_redos(self, san):
        self.redos.append(san)

    def pop_history(self):

        if not self.history:
            return None

        return self.history.pop(0)
    
    def push_history(self, san):
        self.history.append(san)