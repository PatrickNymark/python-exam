from bcolors import bcolors 

class Box():
    def __init__(self, position_x, position_y, symbol = '*'):
        self.symbol = symbol
        self.hit = False
        self.is_ship = False
        self.position_x = position_x
        self.position_y = position_y
    
    def change_to_ship(self):
        self.symbol = '@'
        self.is_ship = True

    def change_to_hit(self):
        self.symbol = 'X'
        self.hit = True

    def anonymous_format(self, anonymous):
        if self.hit:
            return f"|{bcolors.FAIL} {self.symbol} {bcolors.ENDC}|"
        else:
            return f"|{bcolors.HEADER} * {bcolors.ENDC}|"

    def __str__(self):
        if self.hit:
            return f"|{bcolors.FAIL} {self.symbol} {bcolors.ENDC}|"
        elif self.is_ship:
            return f"|{bcolors.OKGREEN} {self.symbol} {bcolors.ENDC}|"
        else:
            return f"|{bcolors.HEADER} {self.symbol} {bcolors.ENDC}|"
    
    def __repr__(self):
        return f"Box({self.position_x, self.position_y})"
