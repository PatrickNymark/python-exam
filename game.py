import os
import game_options

class Game:
    """
    Attributes:
        players (list): including 2 player instances.
    """
    def __init__(self, players):
        self.players = players
        self.turns = 0

    def start_game(self):
        """
        Starts the game, and runs until one player has won
        """
        # for player in self.players:
        #     player.initialize_ships()
        self.initialize_game()
    
        while True:
            current_turn = self.get_current_turn()
            current = current_turn[0]
            opponent = current_turn[1]
            
            input("\n" + current.name + ", please enter if you are ready! \n")
            game_options.make_move_options(current_turn)

            coordinate_input = input("Coordinates to attack: ")
            coordinates = [int(x) for x in coordinate_input.split(",")]

            # make move on opponents board
            result = opponent.board.make_move(coordinates)

            if result:
                if current_turn[1].board.check_if_fleet_sunken():
                    print("\n")
                    print("All ships are down! \nYou have won!")
                    break
            
            self.turns += 1

    def initialize_game(self):
        """ creates all entries for the board and ships for each player"""
        for player in self.players:
            player.board.initialize_board()
            player.initialize_ships()

    def get_current_turn(self):
        """ returns the current turn"""
        if self.turns % 2 == 0:
            return [self.players[0], self.players[1]]
        else:
            return [self.players[1], self.players[0]]


