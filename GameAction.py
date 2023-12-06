class Turn:

    current_turn = 1

    def __init__(self, player) -> None:
        self.player = player
        Turn.current_turn += 1 
        
        if str(player) == "1":
            self.avail_workers = "AB"
            self.color = "white"
        else:
            self.avail_workers = "YZ"
            self.color = "blue"

    def __repr__(self):
        return f"Turn: {Turn.current_turn - 1}, {self.color} ({self.avail_workers})"

class Move:
    def __init__(self, worker, move_dir, build_dir) -> None:
        self.worker = worker
        self.move_dir = move_dir
        self.build_dir = build_dir

    def __repr__(self) -> str:
        return f"{self.worker} {self.move_dir} {self.build_dir}"

class GameAction: 
    def __init__(self, san) -> None:
        self.san = san

    def execute(self):
        raise NotImplementedError

class QueryPlayer(GameAction):
    def __init__(self, san) -> None:
        super().__init__(san)

    def execute(self):
        moved_worker = input("Select a worker to move \n")
        move_dir = input("Select a direction to move (n, ne, e, se, s, sw, w, nw) \n")
        build_dir = input("Select a direction to build (n, ne, e, se, s, sw, w, nw) \n")
        print(Move(moved_worker, move_dir, build_dir))
        return Move(moved_worker, move_dir, build_dir)
    
class PrintBoard(GameAction):
    def __init__(self, san, player_turn) -> None:
        super().__init__(san)
        self.player_turn = player_turn

    def execute(self):
        print(Turn(player=self.player_turn))
        print(self.san)