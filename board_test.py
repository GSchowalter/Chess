import board

def test_init(b1):
    assert len(b1.space) == 64, "Should be 64"
    assert b1.space["A8"].color == "w", "A8 should be white"
    space_names = ["A8", 'A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1',
    "B8", 'B7', 'B6', 'B5', 'B4', 'B3', 'B2', 'B1',
    "C8", 'C7', 'C6', 'C5', 'C4', 'C3', 'C2', 'C1',
    "D8", 'D7', 'D6', 'D5', 'D4', 'D3', 'D2', 'D1',
    "E8", 'E7', 'E6', 'E5', 'E4', 'E3', 'E2', 'E1',
    "F8", 'F7', 'F6', 'F5', 'F4', 'F3', 'F2', 'F1',
    "G8", 'G7', 'G6', 'G5', 'G4', 'G3', 'G2', 'G1',
    "H8", 'H7', 'H6', 'H5', 'H4', 'H3', 'H2', 'H1',]
    for space in space_names:
        assert space in b1.space, "Missed {}".format(space)

    i = 0
    for space in b1.space:
        if i % 2 == 0:
            assert b1.space[space].color == 'b', "{} should be w".format(i)
        else:
            assert b1.space[space].color == 'w', "{} should be b".format(space)
        i += 1

if __name__ == "__main__":
    b1 = board.Board()
    test_init(b1)

    print("Everything passed")
