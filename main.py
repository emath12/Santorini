import Santorini as s

class PlayGame:

    def __init__(self):
        self.game = None
    
    def set_game(self, game):
        self.game = game

    def play(self):
        self.game.play()

def main():
    game = PlayGame()

    game.set_game(s.Santorini())
    game.play()

if __name__ == "__main__":
    main()

