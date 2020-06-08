


from board import Board
from player import Player
from game import Game

import os

import game_options
    

fleets = [[('Battleship', 5), ('Carrier', 4), ('Cruiser', 3), ('Destroyer', 3)],
          [('Carrier', 4), ('Destroyer', 3), ('Submarine', 2)],
          [('Destroyer', 3), ('Minesweeper', 2), ('Submarine', 2)]]

def main():
    game_options.clear()
    game_options.initial_options()

    while True:
        option = int(input("Please choose option: "))

        if option == 1:
            # default values
            rows = 5
            cols = 5
            
            board_1 = Board(int(rows), int(cols))
            board_2 = Board(int(rows), int(cols))
1
            board_1.initialize_board()
            board_2.initialize_board()

            player1 = Player("Player One", board_1, fleets[1])
            player2 = Player("Player Two", board_2, fleets[1])
            break

        elif option == 2:
            rows = input('Please enter rows: ')
            cols = input('Please enter columns: ')

            board_1 = Board(int(rows), int(cols))
            board_2 = Board(int(rows), int(cols))

            board_1.initialize_board()
            board_2.initialize_board()

            game_options.fleets_options(fleets)
            fleet_input = int(input("Please enter option: "))

            player1 = Player(input('Please enter name of player 1: '), board_1, fleets[fleet_input])
            player2 = Player(input('Please enter name of player 2: '), board_2, fleets[fleet_input])
            break

        else:
            print("\nPlease enter valid option: ")
            print("\n1 - Quick start")
            print("2 - Custom Game \n")
    
    game = Game([player1, player2])
    game.start_game()


if __name__ == "__main__":
    main()






