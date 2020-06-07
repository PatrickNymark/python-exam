import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def initial_options():
    print(r"""
                                    |__
                                    |\/
                                    ---
                                    / | [
                             !      | |||
                           _/|     _/|-++'
                       +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
    __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
    |                        Welcome to Battleship                         BB-61/
    \_________________________________________________________________________|""" + "\n")

    print("1 - Quick start")
    print("2 - Custom Game \n")


def fleet_options():
    print("\nYou have following ships:")
    print(" - Carrier    : 4")
    print(" - Destroyer  : 3")
    print(" - Battleship : 2")

    print("\nFormat x,y")
    print("Example: 1,1 \n")
    

def make_move_options(players):
    clear()
    print(f"{players[0].name}, its your turn to make a move: ")
    print(f"\nEnemy board: ")
    players[1].board.print_board(True)
    print(f"\nOwn board: ")
    players[0].board.print_board()
