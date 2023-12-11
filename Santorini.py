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
        self._board : Board = Board()
        self._current_turn : Turn = None
        self._current_player : Player = None
        self._player_1_type = player_1_type
        self._player_2_type = player_2_type

        self._worker_Y = self._board[1, 1].piece
        self._worker_B = self._board[1, 3].piece
        self._worker_A = self._board[3, 1].piece
        self._worker_Z = self._board[3, 3].piece 

        self._winner = None
        self._undo_redo_enabled = undo_redo_enabled
        self._enabled_display_score = enabled_display_score

        self._players = []
        self._history = History()

        if player_1_type == PlayerType.HUMAN:
            self._players.append(Player(board=self._board, color="white", workers=[self._worker_A, self._worker_B]))
        elif player_1_type == PlayerType.RANDOM:
            self._players.append(RandomPlayer(board=self._board, color="white", workers=[self._worker_A, self._worker_B]))
        else:
            self._players.append(HeurisiticPlayer(board=self._board, color="white", workers=[self._worker_A, self._worker_B]))

        if player_2_type == PlayerType.HUMAN:
            self._players.append(Player(board=self._board, color="blue", workers=[self._worker_Y, self._worker_Z]))
        elif player_2_type == PlayerType.RANDOM:
            self._players.append(RandomPlayer(board=self._board, color="blue", workers=[self._worker_Y, self._worker_Z]))
        else:
            self._players.append(HeurisiticPlayer(board=self._board, color="blue", workers=[self._worker_Y, self._worker_Z]))

        self._history = History()

    def _isWinner(self):

        if not any(worker.can_move() for worker in self._current_player.workers):
            return [True, None]

        for index, ele in self._board:
            if ele.height == 3 and ele.piece:
                return [True, ele.piece.owner]
        
        return [False, None]
    
    def _print_round(self):
        
        print(self._board)
        self._current_player.get_my_score()

        if self._enabled_display_score:
            print(self._current_turn, end = ", ")
            print(self._current_player.score)
        else:
            print(self._current_turn)

        if self._undo_redo_enabled:
            undo = input("undo, redo, or next\n")

            if undo == "redo":
                self._restore(self._history.pop_redos())
                self._print_round()
            elif undo == "undo":
                self._history.push_redos(self._get_state())
                self._restore(self._history.pop_history())
                self._print_round()

    def _play(self):
        self._current_turn = Turn(
            player=self._players[0], 
        )

        self._current_player : Player = self._players[0]
        
        while True:            

            self._print_round()

            if self._isWinner()[0]:
                break
            self._save()

            made_move = self._current_player.make_move()

            if self._enabled_display_score:
                print(made_move, end = " ")
                print(made_move.move_score)
            else:
                print(made_move)

            if self._current_player.color == "blue":
                self._current_turn = Turn(player=self._players[0])
                self._current_player = self._players[0]
            else:
                self._current_turn = Turn(player=self._players[1])
                self._current_player = self._players[1]

        if self._current_player.color == "blue":
            print("white has won")
        else:
            print("blue has won")
        
        play_again = input("Play again?\n")

        if play_again == "yes":
            s = Santorini(player_1_type=self._player_1_type, 
                      player_2_type=self._player_2_type, 
                      undo_redo_enabled=self._undo_redo_enabled,
                      enabled_display_score=self._enabled_display_score
            )

            Turn.current_turn = 1
            s._play()
        else:
            sys.exit()

    def _get_state(self):
        s = SantoriniState(
            
            player_1_type=self._player_1_type,
            player_2_type=self._player_2_type,
            current_turn=self._current_turn.current_turn,
            current_player=self._current_player,
            players=copy.deepcopy(self._players),
            board=copy.deepcopy(self._board),
            undo_redo_enabled=self._undo_redo_enabled,
            enabled_display_score=self._enabled_display_score,
            worker_Y=copy.deepcopy(self._worker_Y),
            worker_A=copy.deepcopy(self._worker_A),
            worker_Z=copy.deepcopy(self._worker_Z),
            worker_B=copy.deepcopy(self._worker_B)
        )

        return s

    def _save(self):

        self._history.push_history(self._get_state())
        
    def _restore(self, san):

        s : SantoriniState = san

        if not s:
            return

        self._board = s.new_board
        self._current_player = s.current_player
        self._worker_A = s.worker_A
        self._worker_B = s.worker_B
        self._worker_Z = s.worker_Z
        self._worker_Y = s.worker_Y
