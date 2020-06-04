import os
import game_options
ships = [ ('Carrier', 4), ('Destroyer', 3), ('Battleshhip', 2)]
ships = [ ('Carrier', 2),]

class Game:
    def __init__(self, players):
        self.players = players
        self.turns = 0

    def start_game(self):
        for player in self.players:
            self.initialize_ships(player)
            print(player.board.ships)
        

        while True:
            current_turn = self.get_current_turn()
            input("\n" + current_turn[0].name + ", please enter if you are ready! \n")
            make_move_options(current_turn)

            coordinate_input = input("Coordinates to attack: ")
            coordinates = [int(x) for x in coordinate_input.split(",")]

            is_hit = current_turn[1].board.make_move(coordinates)

            if is_hit:
                print("\nHit! \n")
            else:
                print("\nMiss! \n")

            self.turns += 1
            
    def initialize_ships(self, player):
        game_options.fleet_options()

        input(player.name + ", please enter if you are ready!")

    
            

        for ship in ships:
            ship_coordinates = []

            player.board.print_board()
            while True:
                coordinates = input(f"Please enter coordinates for ship {ship[0]}: ")
                
                ship_coordinates.append([int(n) for n in coordinates.split(",")])
                
                if len(ship_coordinates) == ship[1]:
                    break
            
           
            player.board.new_ship(ship_coordinates)
        
                

    def get_current_turn(self):
        if self.turns % 2 == 0:
            return [self.players[0], self.players[1]]
        else:
            return [self.players[1], self.players[0]]

    # def get_opponent(self):
    #     if self.get_player_turn() == 0:
    #         return self.players[1]
    #     else:
    #         return self.players[0]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def make_move_options(players):
    clear()
    print(f"{players[0].name}, its your turn to make a move: ")
    print(f"\nEnemy board: ")
    players[1].board.print_board(True)
    print(f"\nOwn board: ")
    players[0].board.print_board()
