import Move
import FEN_utils

class Game:
    position = ""
    board = [["-" for i in range(8)] for j in range(8)] 
    def __init__(self, position="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.position = position
        self.initialize_board(position)

    def split(self, word):
        return [char for char in word]

    def parse_fen_rank(self, rank):
        new_rank = []
        for space in rank:
            if space.isnumeric():
                for empty_space in range(int(space)):
                    new_rank = new_rank + ["-"]
            else:
                new_rank = new_rank + [space]
        return new_rank


    def initialize_board(self, position):
        fen = FEN_utils.parse_FEN(position)
        raw_ranks = fen[0:8]
        ranks = []
        for rank in raw_ranks:
            rank_list = self.split(rank)
            ranks.append(rank_list)
        
        # convert numbers to empty spaces
        for count, rank in enumerate(ranks):
            new_rank = self.parse_fen_rank(rank)
            self.board[count] = new_rank

    def move(self, move):
        if Move.move_is_legal(self.position, move):
            self.position = Move.transform_position(self.position, move)
        else:
            raise Move.IllegalMoveException()

    def pretty_print_rank(self, rank):
        left = "|_"
        right = "_"
        rank_str = ""
        for square in rank:
            if square.isnumeric():
                for space in range(int(square)):
                    rank_str = rank_str + "{}_{}".format(left, right)
            else:
                rank_str = rank_str + "{}{}{}".format(left, square, right)
        rank_str += "|"
        return rank_str
    """
    _________________________________
    |_r_|_n_|_b_|_q_|_k_|_b_|_n_|_r_|
    |_p_|_p_|_p_|_p_|_p_|_p_|_p_|_p_|
    |___|___|___|___|___|___|___|___|
    |___|___|___|___|___|___|___|___|
    |___|___|___|___|___|___|___|___|
    |___|___|___|___|___|___|___|___|
    |_P_|_P_|_P_|_P_|_P_|_P_|_P_|_P_|
    |_R_|_N_|_B_|_Q_|_K_|_B_|_N_|_R_|
    """
    def pretty_print_position(self):
        top = "_________________________________"

        ranks = self.position.split("/")
        eigth = ranks[0]
        seventh = ranks[1]
        sixth = ranks[2]
        fifth = ranks[3]
        fourth = ranks[4]
        third = ranks[5]
        second = ranks[6]
        first = ranks[7].split(" ")[0]
        
        eigth_str = self.pretty_print_rank(eigth)
        seventh_str = self.pretty_print_rank(seventh)
        sixth_str = self.pretty_print_rank(sixth)
        fifth_str = self.pretty_print_rank(fifth)
        fourth_str = self.pretty_print_rank(fourth)
        third_str = self.pretty_print_rank(third)
        second_str = self.pretty_print_rank(second)
        first_str = self.pretty_print_rank(first)

        board_str = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(top, eigth_str, seventh_str, sixth_str, fifth_str, fourth_str, third_str, second_str, first_str)
        return board_str