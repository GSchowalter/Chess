from piece import Piece
import space

class Board:

    def __init__(self):
        self.space = dict()
        self.color = dict()

        space_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

        for i in range(71, 7, -1):
            self.space[space_letters[i % 8] + str(i//8)] = space.Space('w', None) if i % 2 == 0 else space.Space('b', None)

        # Initialize a standard board 
        # TODO: change to accept FEN notation
        self.initialize_standard_setup()


    def initialize_standard_setup(self):
        self.space['A8'].set_piece(Piece('b', 'r'))
        self.space['B8'].set_piece(Piece('b', 'n'))
        self.space['C8'].set_piece(Piece('b', 'b'))
        self.space['D8'].set_piece(Piece('b', 'q'))
        self.space['E8'].set_piece(Piece('b', 'k'))
        self.space['F8'].set_piece(Piece('b', 'b'))
        self.space['G8'].set_piece(Piece('b', 'n'))
        self.space['H8'].set_piece(Piece('b', 'r'))

        self.space['A7'].set_piece(Piece('b', 'p'))
        self.space['B7'].set_piece(Piece('b', 'p'))
        self.space['C7'].set_piece(Piece('b', 'p'))
        self.space['D7'].set_piece(Piece('b', 'p'))
        self.space['E7'].set_piece(Piece('b', 'p'))
        self.space['F7'].set_piece(Piece('b', 'p'))
        self.space['G7'].set_piece(Piece('b', 'p'))
        self.space['H7'].set_piece(Piece('b', 'p'))

        self.space['A1'].set_piece(Piece('w', 'r'))
        self.space['B1'].set_piece(Piece('w', 'n'))
        self.space['C1'].set_piece(Piece('w', 'b'))
        self.space['D1'].set_piece(Piece('w', 'q'))
        self.space['E1'].set_piece(Piece('w', 'k'))
        self.space['F1'].set_piece(Piece('w', 'b'))
        self.space['G1'].set_piece(Piece('w', 'n'))
        self.space['H1'].set_piece(Piece('w', 'r'))

        self.space['A2'].set_piece(Piece('b', 'p'))
        self.space['B2'].set_piece(Piece('b', 'p'))
        self.space['C2'].set_piece(Piece('b', 'p'))
        self.space['D2'].set_piece(Piece('b', 'p'))
        self.space['E2'].set_piece(Piece('b', 'p'))
        self.space['F2'].set_piece(Piece('b', 'p'))
        self.space['G2'].set_piece(Piece('b', 'p'))
        self.space['H2'].set_piece(Piece('b', 'p'))