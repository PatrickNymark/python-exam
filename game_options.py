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

def fleets_options(fleets):
    print("\nYou have following fleets to choose from: ")
    for i in range(len(fleets)):
        print(f"{i + 1} -", *fleets[i])

def fleet_options(fleet):
    clear()
    print("\nYou have following ships:")
    for i in range(len(fleet)):
        print(f"{i + 1} - {fleet[i][0]}: {fleet[i][1]}")
        
    print("\nFormat x,y")
    print("Example: 1,1 \n")

def game_over(winner, opponent):
    print("\n")

    print(f"All ships are down! \n{winner.name} have won!\n")
    
    print(f"{winner.name} board:")
    winner.board.print_board()
    print(f"{opponent.name} board:")
    opponent.board.print_board()


def make_move_options(players):
    clear()
    board_options()
    print(f"{players[0].name}, its your turn to make a move: ")
    print(f"\nEnemy board: ")
    players[1].board.print_board(True)
    print(f"\nOwn board: ")
    players[0].board.print_board()

def board_options():
    print("\n")
    print("X: Ship sunken")
    print("/: Ship coordinate hit")
    print("@: Ship coordinate for players own board")
    print("\n")