import Move

def test_move_is_legal():

    initial= "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    efour = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

    """
    rnbqkbnr    rnbqkbnr
    pppppppp    pppppppp
    8           8
    8           8
    8           4P3         8           4P3
    8           8
    PPPPPPPP    PPPP1PPP    PPPPPPPP    PPPP1PPP
    RNBQKBNR    RNBQKBNR
    """

    assert Move.move_is_legal(initial, efour), "legal move marked as illegal"



if __name__ == "__main__":
    test_move_is_legal()
    print("Everything passed")