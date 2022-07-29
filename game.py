class Game:
    starting_position = ""
    def __init__(self, starting_postion="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.starting_position = starting_postion

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

        ranks = self.starting_position.split("/")
        eigth = ranks[0]
        seventh = ranks[1]
        sixth = ranks[2]
        fifth = ranks[3]
        fourth = ranks[4]
        third = ranks[5]
        second = ranks[6]
        first = ranks[7]
            
        print("ranks:", ranks)
        return "_________________________________\n|_r_|_n_|_b_|_q_|_k_|_b_|_n_|_r_|\n|_p_|_p_|_p_|_p_|_p_|_p_|_p_|_p_|\n|___|___|___|___|___|___|___|___|\n|___|___|___|___|___|___|___|___|\n|___|___|___|___|___|___|___|___|\n|___|___|___|___|___|___|___|___|\n|_P_|_P_|_P_|_P_|_P_|_P_|_P_|_P_|\n|_R_|_N_|_B_|_Q_|_K_|_B_|_N_|_R_|"
        