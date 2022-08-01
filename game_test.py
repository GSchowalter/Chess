from Game import Game

def test_initialize_board():
    expected = [
      ["r", "n", 'b', 'q', 'k', 'b', 'n', 'r'],
      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
      ['-', '-', '-', '-', '-', '-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-', '-'],
      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
      ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
    game = Game()
    actual = game.board

    assert expected == actual, "Board not initialized correctly. Actual...\n" + str(actual) + "\nExpected...\n" + str(expected)

    london_game = Game(position="rnbqkb1r/pp2pppp/5n2/2pp4/3P1B2/4P3/PPP2PPP/RN1QKBNR b KQkq - 0 1")
    london_actual = london_game.board
    london_expected = [
      ["r", "n", 'b', 'q', 'k', 'b', '-', 'r'],
      ['p', 'p', '-', '-', 'p', 'p', 'p', 'p'],
      ['-', '-', '-', '-', '-', 'n', '-', '-'],
      ['-', '-', 'p', 'p', '-', '-', '-', '-'],
      ['-', '-', '-', 'P', '-', 'B', '-', '-'],
      ['-', '-', '-', '-', 'P', '-', '-', '-'],
      ['P', 'P', 'P', '-', '-', 'P', 'P', 'P'],
      ['R', 'N', '-', 'Q', 'K', 'B', 'N', 'R']
    ]

    assert london_actual == london_expected, "London board not initialized correctly. Actual...\n" + str(london_actual) + "\nExpected...\n" + str(london_expected)

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
    assert actual == expected, "Pretty print not working for starting position \n" + actual + "\n\nexpected\n" + expected

    london_game = Game(position="rnbqkb1r/pp2pppp/5n2/2pp4/3P1B2/4P3/PPP2PPP/RN1QKBNR b KQkq - 0 1")
    actual = london_game.pretty_print_position()
    expected = "_________________________________\n|_r_|_n_|_b_|_q_|_k_|_b_|___|_r_|\n|_p_|_p_|___|___|_p_|_p_|_p_|_p_|\n|___|___|___|___|___|_n_|___|___|\n|___|___|_p_|_p_|___|___|___|___|\n|___|___|___|_P_|___|_B_|___|___|\n|___|___|___|___|_P_|___|___|___|\n|_P_|_P_|_P_|___|___|_P_|_P_|_P_|\n|_R_|_N_|___|_Q_|_K_|_B_|_N_|_R_|"
    assert actual == expected, "Pretty print not working for London opening actual\n" + actual + "\n\nexpected\n" + expected


if __name__ == "__main__":
    test_initialize_board()
    test_pretty_print()
    print("Everything passed")