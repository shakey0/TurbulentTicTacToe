import secrets


class Board:
    
    def __init__(self, width, height):
        self.id = "board_" + secrets.token_hex(8)
        self.width = width
        self.height = height
        self.spaces = 0
        def get_num():
            self.spaces += 1
            return self.spaces
        self.board = [[[get_num(), '.'] for x in range(width)] for y in range(height)]
