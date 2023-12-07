from constants import TEXT_DIR_TO_NUM

class Turn:

    current_turn = 1

    def __init__(self, player) -> None:
        self.player : 'Player' = player
        Turn.current_turn += 1 
        
        if player.color == "white":
            self.avail_workers = "AB"
            self.color = "white"
        else:
            self.avail_workers = "YZ"
            self.color = "blue"

    def __repr__(self):
        return f"Turn: {Turn.current_turn - 1}, {self.color} ({self.avail_workers})"

class Move:
    def __init__(self, worker, move_dir, build_dir) -> None:
        self.worker : 'Worker' = worker
        self.move_dir : 'Direction' = move_dir
        self.build_dir : 'Direction' = build_dir
        self.num_move_dir = TEXT_DIR_TO_NUM[move_dir]
        self.num_build_dir = TEXT_DIR_TO_NUM[build_dir]

    def __repr__(self) -> str:
        return f"{self.worker} {self.move_dir} {self.build_dir}"