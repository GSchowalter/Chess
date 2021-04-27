class Space:

    def __init__(self, color, piece):
        self.color = color
        self.occupied = False
        self.piece = piece
    
    def set_piece(self, piece):
        self.piece = piece
        self.occupied = True