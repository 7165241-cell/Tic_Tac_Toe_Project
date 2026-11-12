from tic_tac_toe.DATA.win_combinatIons import WINNING_LINES

def check_win(menu_number, symbol):
    for a, b, c in WINNING_LINES:
        if menu_number[a] == symbol and menu_number[b] == symbol and menu_number[c] == symbol:
            return True
    return False
