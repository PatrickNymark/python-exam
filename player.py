import game_options

ships = [ ('Carrier', 2),]


class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def initialize_ships(self):
        """ initializes the entries for all ships
            and adds them to the players game board.
        """
        game_options.fleet_options()

        input(self.name + ", please enter if you are ready!")
    
        for ship in ships:
            ship_coordinates = []

            self.board.print_board()
            while True:
                coordinates = input(f"Please enter coordinates for ship {ship[0]}: ")
                
                ship_coordinates.append([int(n) for n in coordinates.split(",")])
                
                if len(ship_coordinates) == ship[1]:
                    break
            
            self.board.new_ship(ship_coordinates)
            
    def __str__(self):
        return f"Player({self.name})"