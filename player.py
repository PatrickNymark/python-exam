class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def __str__(self):
        return f"Player({self.name})"