


from board import Board
from player import Player
from game import Game

import os

import game_options
    
def main():
    game_options.clear()
    game_options.initial_options()

    option = int(input("Please choose option: "))

    # default values
    rows = 5
    cols = 5

    if option == 1:
        board_1 = Board(int(rows), int(cols))
        board_2 = Board(int(rows), int(cols))

        board_1.initialize_board()
        board_2.initialize_board()

        player1 = Player("Player One", board_1)
        player2 = Player("Player Two", board_2)

    elif option == 2:
        rows = input('Please enter rows: ')
        cols = input('Please enter columns: ')

        board_1 = Board(int(rows), int(cols))
        board_2 = Board(int(rows), int(cols))

        board_1.initialize_board()
        board_2.initialize_board()

        player1 = Player(input('Please enter name of player 1: '), board_1)
        player2 = Player(input('Please enter name of player 2: '), board_2)

    else:
        print("Welcome to Battleship Game")
        print("\n1 - Quick start")
        print("2 - Custom Game \n")

        option = input("Please choose option: ")
    
    game = Game([player1, player2])
    game.start_game()


if __name__ == "__main__":
    main()






