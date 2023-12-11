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
            
            self.board = copy.deepcopy(board)
            self.current_turn : int = current_turn
            self.current_player = copy.deepcopy(current_player)
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
            players[0].board = self.board
            players[1].board = self.board

            self.worker_Y.board = self.board
            self.worker_A.board = self.board
            self.worker_B.board = self.board
            self.worker_Z.board = self.board

class History:

    def __init__(self) -> None:
        self.history = []
        self.history_index = 0

    def pop(self):
        state = self.history.pop(self.history_index)

        self.history_index -= 1 

        return state
    
    def push(self, san):
        self.history.push(san)