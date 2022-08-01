from FEN_utils import parse_FEN

class IllegalMoveException(Exception):
        def __init__(self, message="move to position is illegal"):
            self.message = message
            super().__init__(self.message)


# return a list of legal moves in algebraic notation
def legal_moves(position):
    return []

def transform_position(position, move):
    return None