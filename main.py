from tic_tac_toe.Functions.menu import menu
from tic_tac_toe.Functions.place import place
from tic_tac_toe.Functions.check_win import check_win

def play():
    menu_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = "X"

    for turn in range(9):
        menu(menu_number)
        place(menu_number, player)

        if check_win(menu_number, player):
            menu(menu_number)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"

    menu(menu_number)
    print("Draw!")


while True:
    play()
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        print("Bye!")
        break