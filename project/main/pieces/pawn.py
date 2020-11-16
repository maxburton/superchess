from project.main.pieces.piece import Piece
from project.main.coord import Coord


class Pawn(Piece):
    name = "pawn"
    colour = None

    # Movement
    movement = {}
    is_first_move = True

    def __init__(self, colour):
        super().__init__(colour)
        self.movement = self.add_move_to_dict([Coord(0, 1)], "normal")
        self.movement = self.add_move_to_dict([Coord(0, 2)], "first")
        self.movement = self.add_move_to_dict([Coord(1, 1), Coord(-1, 1)], "attack")
