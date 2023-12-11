from constants import TEXT_DIR_TO_NUM
import copy

class Turn:

    current_turn = 1
    avail_workers = {
        "blue" : "YZ",
        "white" : "AB"
    }

    def __init__(self, color=None) -> None:
        # Turn.player : 'Player' = player
        
        Turn.color = color

    def __repr__(self):
        
        return f"Turn: {Turn.current_turn}, {Turn.color} ({Turn.avail_workers[Turn.color]})"

class Move:
    def __init__(self, worker, move_dir, build_dir) -> None:
        self.worker : 'Worker' = worker
        self.move_dir : 'Direction' = move_dir
        self.build_dir : 'Direction' = build_dir
        self.num_move_dir = TEXT_DIR_TO_NUM[move_dir]
        self.num_build_dir = TEXT_DIR_TO_NUM[build_dir]
        self.move_score = 0

    def get_move_score(self):
        self.move_score = MoveScore(self)
        return self.move_score

    def __repr__(self) -> str:
        return f"{self.worker},{self.move_dir},{self.build_dir}"
    
class MoveScore:
    def __init__(self, move: Move):

        self.height_score = None
        self.center_score = None
        self.distance_score = None
        self.winning_move = False


        self.c1 = 3
        self.c2 = 2
        self.c3 = 1

        new_board = copy.deepcopy(move.worker.board)
        new_moved_worker = copy.deepcopy(move.worker)

        new_board.move_worker(new_moved_worker, move.move_dir)
        new_board.build(new_moved_worker, move.build_dir)

        self.my_other_worker = None
        self.enemy_workers = []


        if move.worker.label == "A":
            self.my_other_worker = new_board.worker_B
            self.enemy_workers.append(new_board.worker_Z)
            self.enemy_workers.append(new_board.worker_Y)
        elif move.worker.label == "B":
            self.my_other_worker = new_board.worker_A
            self.enemy_workers.append(new_board.worker_Z)
            self.enemy_workers.append(new_board.worker_Y)
        elif move.worker.label == "Y":
            self.my_other_worker = new_board.worker_Z
            self.enemy_workers.append(new_board.worker_A)
            self.enemy_workers.append(new_board.worker_B)
        else:
            self.my_other_worker = new_board.worker_Y
            self.enemy_workers.append(new_board.worker_A)
            self.enemy_workers.append(new_board.worker_B)

        def calculate_height_score():

            height_score = 0

            for worker in [new_moved_worker, self.my_other_worker]:
                height_score += new_board[worker.coords].height

            return height_score
    
        self.height_score = calculate_height_score()

        def calculate_center_score():
            
            center_score = 0

            for worker in [new_moved_worker, self.my_other_worker]:

                if worker.coords == [2, 2]:
                    center_score += 2 
                elif worker.coords in [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [3, 3]]:
                    center_score += 1
                else:
                    center_score += 0

            return center_score
        
        self.center_score = calculate_center_score()

        def calculate_distance_score():

            def chebyshev_distance(point1, point2):
                x1, y1 = point1
                x2, y2 = point2
                return max(abs(x1 - x2), abs(y1 - y2))

            distance_score = min(
                chebyshev_distance(new_moved_worker.coords, self.enemy_workers[0].coords),
                chebyshev_distance(self.my_other_worker.coords, self.enemy_workers[0].coords),
            ) + min (
                chebyshev_distance(new_moved_worker.coords, self.enemy_workers[1].coords),
                chebyshev_distance(self.my_other_worker.coords, self.enemy_workers[1].coords),
            )

            distance_score = 8 - distance_score

            return distance_score
        
        self.distance_score = calculate_distance_score()

        if new_board[new_moved_worker.coords].height == 3:
            self.winning_move = True

    def get_move_score(self):
        if self.winning_move:
            return float("+inf")
        return self.c1*self.height_score + self.c2*self.center_score + self.c3*self.distance_score
        
    def __str__(self) -> str:
        return f"({self.height_score}, {self.center_score}, {self.distance_score})"
    def __repr__(self) -> str:
        return f"({self.height_score}, {self.center_score}, {self.distance_score})"
    
    
    
    