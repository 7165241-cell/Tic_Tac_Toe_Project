from tic_tac_toe.Validations.input import input_number


def place(menu_number, symbol):
    while True:
        number = input_number(f"Player {symbol}, please choose a number (1-9): ")
        cell = menu_number[number - 1]

        if cell != "X" and cell != "O":
            menu_number[number - 1] = symbol
            return
        print("This cell is already taken choose another one.")
