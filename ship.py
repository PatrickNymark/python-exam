class Ship():
    def __init__(self, entries):
        self.entries = entries
        self.sunken = False

    def check_if_hit(self, coordinates):
        for entry in self.entries:
            if entry.position_x == coordinates[0] and entry.position_y == coordinates[1]:
                if entry.is_ship:
                    entry.change_to_hit()
                    return True
        
        return False
    
    def check_if_sunken(self):
        return all(entry for entry in self.entries if entry.sunken)

    def initialize_entries(self):
        for entry in self.entries:
            entry.change_to_ship()
            
    def __repr__(self):
        return f"Ship({self.entries}, {self.sunken})"