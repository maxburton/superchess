from project.main.pieces.piece import Piece
from project.main.coord import Coord
from project.main.common_coords import cardinal, combine


class Medic(Piece):
    name = "medic"
    colour = None

    # Movement
    movement = {}
    is_first_move = True
    can_attack = False
    is_carrying = False

    def __init__(self, colour):
        super().__init__(colour)
        # can move a cardinal direction once or twice per turn
        self.movement = self.add_move_to_dict(cardinal() + combine(cardinal(), cardinal()), "normal")
        # can immediately jump forward 3 spaces
        self.movement = self.add_move_to_dict([Coord(0, 3)], "first")
        # backwards and diagonal backwards
        self.movement = self.add_move_to_dict([Coord(0, -1), Coord(1, -1), Coord(-1, -1)], "carrying")

    def is_move_valid(self, new_pos):
        pass
