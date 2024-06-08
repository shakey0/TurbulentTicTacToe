class Player:
    
    def __init__(self, name, character):
        self.name = name
        self.character = character
        self.shapes = []
        self.score = 0
        self.turn = False
        self.winner = False
