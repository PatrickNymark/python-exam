from box import Box
from ship import Ship
import game_options

class Board():
    def __init__(self, rows, cols, ships=None):
        self.rows = rows
        self.cols = cols
        if ships is None:
            ships = []

        self.ships = []

    def make_move(self, coordinates):
        game_options.clear()
        
        for ship in self.ships:
            if ship.check_if_hit(coordinates):
                game_options.clear()
                print("Hit!")

                if ship.check_if_sunken():
                    ship.change_to_sunken()
                    print("Ship sunken!") 
                
                return True
        
        print("Miss!")
        return False
        
    def initialize_board(self):
        initialize_boxes = []

        for row in reversed(range(self.rows)): 
            boxes = []
            for col in range(self.cols):
                boxes.append(Box(col + 1, row + 1))

            initialize_boxes.append(boxes)

        self.entries = initialize_boxes
        
    def print_board(self, anonymous = False):
        for idx, row in enumerate(self.entries):
            reversed_idx = len(self.entries) - idx
            output = str(reversed_idx)

            if reversed_idx < 10:
                output += " "
                
            if anonymous:
                print(output, ' '.join(x.anonymous_format() for x in row))
            else:
                print(output, *row)
        
        board_x_coordinates = [str(i + 1) for i in range(self.cols)]
        # make format match the columns in the board print
        spaced_coordinates = '     '.join(board_x_coordinates[0:9])
        spaced_coordinates += "     "
        spaced_coordinates += '    '.join(board_x_coordinates[9:])
        print(f"     {spaced_coordinates} \n")

    def check_if_fleet_sunken(self):
        return all(ship.check_if_sunken() for ship in self.ships)

    def new_ship(self, coordinates):
        entries = []
        ## refactor ##
        for row in self.entries:
            for entry in row:
                for n in coordinates:
                    if entry.position_x == n[0] and entry.position_y == n[1]:
                        entries.append(entry)

        
        ship = Ship(entries)
        ship.initialize_entries()
        self.ships.append(ship)

    # def __str__(self):
    #     return f"Board({self.entries})"