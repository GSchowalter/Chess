# Return the FEN parse into a list where each entry is
#   [0:7] the first eight fields are the ranks from 8-1
#   [8]   active color "w" or "b"
#   [9]   Castling availability "-" for no castling, this field contains one or more letters: "K" if White can castle kingside, "Q" if White can castle queenside, "k" if Black can castle kingside, and "q" if Black can castle queenside. A situation that temporarily prevents castling does not prevent the use of this notation.
#   [10]  En passant target square. Square that a pawn has just pased over when moving two spaces. Recorded regrdless of whether legal en passat is on the board ."-" if no target square.
#   [11]  Halfmove clock: The number of halfmoves since the last capture or pawn advance, used for the fifty-move rule
#   [12]  Fullmove number: The number of the full moves. It starts at 1 and is incremented after Black's move.

def parse_FEN(position):
    ranks = position.split("/")
    conditions = ranks[7].split(" ")[1:12]
    ranks[7] = ranks[7].split(" ")[0]
    return ranks + conditions