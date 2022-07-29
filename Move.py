from FEN_utils import parse_FEN

class IllegalMoveException(Exception):
        def __init__(self, message="move to position is illegal"):
            self.message = message
            super().__init__(self.message)

# Idetify move and return tupple with
#   string in PGN notation (e4, Nc3, 0-0, etc.)
#   piece moved
#   en passant flag
def identify_move(initial_ranks, new_ranks):
    affected_ranks = []
    for rank in range(8):
        if initial_ranks[rank] != new_ranks[rank]:
            affected_ranks.append(rank)
    return "e4"

def move_is_legal(initial_position, new_position):
    initial_fen = parse_FEN(initial_position)
    new_fen = parse_FEN(new_position)
    move = identify_move(initial_fen[0:7], new_fen[0:7])
    return False