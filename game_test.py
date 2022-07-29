from Game import Game

def test_pretty_print():
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
    expected = "_________________________________\n|_r_|_n_|_b_|_q_|_k_|_b_|_n_|_r_|\n|_p_|_p_|_p_|_p_|_p_|_p_|_p_|_p_|\n|___|___|___|___|___|___|___|___|\n|___|___|___|___|___|___|___|___|\n|___|___|___|___|___|___|___|___|\n|___|___|___|___|___|___|___|___|\n|_P_|_P_|_P_|_P_|_P_|_P_|_P_|_P_|\n|_R_|_N_|_B_|_Q_|_K_|_B_|_N_|_R_|"
    game = Game()
    actual = game.pretty_print_position()

    assert actual == expected, "Pretty print not working: actual\n" + actual + "\n\nexpected\n" + expected



if __name__ == "__main__":
    test_pretty_print()
    print("Everything passed")