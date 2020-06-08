import game_options

class Player:
    def __init__(self, name, board, fleet):
        self.name = name
        self.board = board
        self.fleet = fleet

    def initialize_ships(self):
        """ initializes the entries for all ships
            and adds them to the players game board.
        """
        game_options.fleet_options(self.fleet)

        input(self.name + ", please enter if you are ready!")
    
        for ship in self.fleet:
            ship_coordinates = []

            self.board.print_board()
            while True:
                coordinates = input(f"Please enter coordinates for ship {ship[0]}: ")
                
                numbered_coordinates = [int(n) for n in coordinates.split(",")]

                if self.check_if_valid_ship(ship_coordinates, numbered_coordinates):
                    ship_coordinates.append(numbered_coordinates)
                
                # we have added all coordinates for the current ship
                if len(ship_coordinates) == ship[1]:
                    break
            
            self.board.new_ship(ship_coordinates)
            

    def check_if_valid_ship(self, ship_coordinates, new_coordinate):
        """ 
            Checks if coordinates including the new coordinate is consecutive on either the x or the y axis.
            This includes checking for duplicates, since if there is a duplicate the numbers wont be consecutive
            on either axis.
        """
        # first coordinate - skip validation
        if len(ship_coordinates) == 0:
            return True

        # to not mutate the original list we add the new coordinate to a temporary list
        total_coordinates = [ship for ship in ship_coordinates]
        total_coordinates.append(new_coordinate)

        x_positions = [x[0] for x in total_coordinates]
        y_positions = [y[1] for y in total_coordinates]

        if sorted(x_positions) == list(range(min(x_positions), max(x_positions)+1)) or sorted(y_positions) == list(range(min(y_positions), max(y_positions)+1)):
            return True
        
        return False

    def __str__(self):
        return f"Player({self.name})"