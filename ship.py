class Ship():
    def __init__(self, entries):
        """
            entries (list): represents a list Box instances used for coordinates on the board
        """
        self.entries = entries

    def check_if_hit(self, coordinates):
        for entry in self.entries:
            if entry.position_x == coordinates[0] and entry.position_y == coordinates[1]:
                if entry.is_ship:
                    entry.change_to_hit()
                    return True
        
        return False
    
    def check_if_sunken(self):
        """ returns true if all entries are hit else false"""
        return all(entry.is_hit for entry in self.entries)

    def change_to_sunken(self):
        """
            Changes all entries to sunken symbol
        """
        for entry in self.entries:
            entry.change_to_sunken()

    def initialize_entries(self):
        """ 
            Once ship is created, this is used to initialize all entries and change to ship symbol
        """
        for entry in self.entries:
            entry.change_to_ship()
            
    def __repr__(self):
        return f"Ship({self.entries}, {self.sunken})"