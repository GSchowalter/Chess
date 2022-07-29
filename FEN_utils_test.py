import FEN_utils

def test_parse_FEN():

    initial= "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    efour = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

    expected = ["rnbqkbnr", "pppppppp", "8", "8", "8", "8", "PPPPPPPP", "RNBQKBNR", "w", "KQkq", "-", "0", "1"]
    actual = FEN_utils.parse_FEN(initial)

    assert expected == actual, "Parse failed actual\n" + str(actual) + "\nexpected\n" + str(expected)



if __name__ == "__main__":
    test_parse_FEN()
    print("Everything passed")