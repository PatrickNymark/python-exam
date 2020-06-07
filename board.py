from box import Box
from ship import Ship

class Board():
    def __init__(self, rows, cols, ships=None):
        self.rows = rows
        self.cols = cols
        if ships is None:
            ships = []

        self.ships = []

    def make_move(self, coordinates):
        for ship in self.ships:
            if ship.check_if_hit(coordinates):
                print("Hit!")

                if ship.check_if_sunken():
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

            if anonymous:
                print(reversed_idx, ' '.join(x.anonymous_format(True) for x in row))
            else:
                print(reversed_idx, *row)
                
        board_x_coordinates = [str(i + 1) for i in range(self.cols)]
        spaced_coordinates = '     '.join(board_x_coordinates)
        print(f"    {spaced_coordinates} \n")

    def check_if_fleet_sunken(self):
        for ship in self.ships:
            if ship.sunken:
                return True


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