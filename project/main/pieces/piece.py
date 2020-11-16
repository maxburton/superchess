class Piece:
    name = None
    colour = None
    movement = None
    can_attack = True

    def __init__(self, colour):
        self.colour = colour

    def add_move_to_dict(self, coords, move):
        for coord in coords:
            if coord in self.movement:
                self.movement[coord] = self.movement[coord] + [move]
            else:
                self.movement[coord] = [move]
        return self.movement
