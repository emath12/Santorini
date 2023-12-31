Santorini is a chess-like strategy game. I created this project as a demonstration of my understnding of Object Oriented Programming. It employs several standard design patterns, as well as
DS&A techniques like combination generation. See the UML diagram and design patterns write up for more info.

Rules:
- Each player, colored blue and white, starts with two workers.
- Workers can move either north, south, east, west, northwest, northeast, southeast, or southwest. 
- Workers can build in any direction in any occupied square.
- The game is won when we build a tower of level 3 and get a worker on it.
- A tower of level 4 cannot have a worker moved onto it.
- Players can build onto a tower of any level, but may only move up one level and down any number of levels.

Commence the game with the following arguments after pulling the git repo

python main.py [player_1_type] [player_2_type] [score on] [undo_redo_on]

player types:
- random (chooses a random move out of a set of avalaible ones)
- human (consumes CLI arguements to move the pieces)
- heurisitc (chooses a best move based on a couple factors)

undo-redo
- on : enable
- off : disable (default)

score-on : display the score of each player's board
- on : enable
- off disable
