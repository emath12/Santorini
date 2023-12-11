# state / mementon - undo/redo
# strategy - type of Santontoi Game
# decorator - print_round for args :
# template - execute play + diff games imp it




# abstract factory, composite (?)

from GameComponent import Board, BoardSquare, Direction, Worker
from GameActions import Turn, Move
from Player import Player, HeurisiticPlayer, RandomPlayer
from exceptions import InvalidWorker, NotYourWorker, InvalidDirection, InvalidMovementDirection, InvalidBuildDirection, WorkerCannotMove
from constants import *
from Player import PlayerType
import copy
import sys
from History import SantoriniState, History 

class Santorini:

    def __init__(self, player_1_type, player_2_type, undo_redo_enabled=False, enabled_display_score=False): 
        self.board : Board = Board()
        self.current_turn : Turn = None
        self.current_player : Player = None
        self.player_1_type = player_1_type
        self.player_2_type = player_2_type

        self.worker_Y = self.board[1, 1].piece
        self.worker_B = self.board[1, 3].piece
        self.worker_A = self.board[3, 1].piece
        self.worker_Z = self.board[3, 3].piece 

        self.winner = None
        self.undo_redo_enabled = undo_redo_enabled
        self.enabled_display_score = enabled_display_score

        self.players = []

        if player_1_type == PlayerType.HUMAN:
            self.players.append(Player(board=self.board, color="white", workers=[self.worker_A, self.worker_B]))
        elif player_1_type == PlayerType.RANDOM:
            self.players.append(RandomPlayer(board=self.board, color="white", workers=[self.worker_A, self.worker_B]))
        else:
            self.players.append(HeurisiticPlayer(board=self.board, color="white", workers=[self.worker_A, self.worker_B]))

        if player_2_type == PlayerType.HUMAN:
            self.players.append(Player(board=self.board, color="blue", workers=[self.worker_Y, self.worker_Z]))
        elif player_2_type == PlayerType.RANDOM:
            self.players.append(RandomPlayer(board=self.board, color="blue", workers=[self.worker_Y, self.worker_Z]))
        else:
            self.players.append(HeurisiticPlayer(board=self.board, color="blue", workers=[self.worker_Y, self.worker_Z]))

        self.history = History()

    def isWinner(self):

        if not any(worker.can_move() for worker in self.current_player.workers):
            return [True, None]

        for index, ele in self.board:
            if ele.height == 3 and ele.piece:
                return [True, ele.piece.owner]
        
        return [False, None]
    
    def print_round(self):
        
        print(self.board)
        self.current_player.get_my_score()

        if self.enabled_display_score:
            print(self.current_turn, end = ", ")
            print(self.current_player.score)
        else:
            print(self.current_turn)

    def play(self):
        self.current_turn = Turn(
            player=self.players[0], 
        )

        self.current_player : Player = self.players[0]
        # self.print_round()
        
        while True:            

            self.print_round()

            if self.isWinner()[0]:
                break

            made_move = self.current_player.make_move()

            if self.enabled_display_score:
                print(made_move, end = " ")
                print(made_move.move_score)
            else:
                print(made_move)

            if self.current_player.color == "blue":
                self.current_turn = Turn(player=self.players[0])
                self.current_player = self.players[0]
            else:
                self.current_turn = Turn(player=self.players[1])
                self.current_player = self.players[1]

        if self.current_player.color == "blue":
            print("white has won")
        else:
            print("blue has won")
        
        play_again = input("Play again?\n")

        if play_again == "yes":
            s = Santorini(player_1_type=self.player_1_type, 
                      player_2_type=self.player_2_type, 
                      undo_redo_enabled=self.undo_redo_enabled,
                      enabled_display_score=self.enabled_display_score
            )

            s.play()
            Turn.current_turn = 1
        else:
            sys.exit()

    def save(self):
        SantoriniState(
            player_1_type=self.player_1_type,
            player_2_type=self.player_2_type,
            current_turn=self.current_turn.current_turn,
            current_player=self.current_player,
            players=self.players,
            board=self.board,
            undo_redo_enabled=self.undo_redo_enabled,
            enabled_display_score=self.enabled_display_score,
            worker_Y=self.worker_Y,
            worker_A=self.worker_A,
            worker_Z=self.worker_Z,
            worker_B=self.worker_B
        )

    def restore():
        pass

    def __deepcopy__(self, memo):
        
        new_board = copy.deepcopy(self.board)

        Santorini(
            board=new_board,
        )