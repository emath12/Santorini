import Santorini as s
import argparse
from GameComponent import Worker, Board
from enum import Enum
from Player import PlayerType



class PlayGame: 

    def __init__(self):
        self.game = None
    
    def set_game(self, game):
        self.game = game

    def play(self):
        self.game.play()

def main():

    game = PlayGame()

    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", type=str, default="human")
    parser.add_argument("arg2", type=str, default="human")
    parser.add_argument("arg3", type=str, default="off")
    parser.add_argument("arg4", type=str, default="off")

    args = parser.parse_args()
    
    player_1 = None
    player_2 = None
    undo_redo_enabled = None
    score_display_enabled = None

    if args.arg1 == "human":
        player_1 = PlayerType.HUMAN
    elif args.arg1 == "random":
        player_1 = PlayerType.RANDOM
    elif args.arg1 == "heuristic":
        player_1 = PlayerType.HEURISTIC
    
    if args.arg2 == "human":
        player_2 = PlayerType.HUMAN
    elif args.arg2 == "random":
        player_2 = PlayerType.RANDOM
    elif args.arg2 == "heuristic":
        player_2 = PlayerType.HEURISTIC


    if args.arg3 == "on":
        undo_redo_enabled = True
    elif args.arg3 == "off":
        undo_redo_enabled = False

    if args.arg4 == "on":
        score_display_enabled = True
    elif args.arg4 == "off":
        score_display_enabled = False


    game.set_game(
        s.Santorini(
            player_1_type=player_1, 
            player_2_type=player_2, 
            undo_redo_enabled=undo_redo_enabled, 
            enabled_display_score=score_display_enabled
        )
    )
    game.play()

if __name__ == "__main__":
    main()

