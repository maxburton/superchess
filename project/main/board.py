from project.main.coord import Coord


piece_mapping = {
    "pawn": " P ",
    "medic": " + ",
}


class Board:
    def __init__(self, size=Coord(8, 8)):
        self.size = size
        self.piece_coords = {}
        self.dead_pieces = []

        self.is_wounded_on = False
        self.wounded_coords = {}


    def get_from_coord(self, coord):
        return self.piece_coords.get(coord)

    def add_piece(self, piece, coord):
        self.piece_coords[coord] = piece

    def move_piece(self, piece, new_coord, old_coord):
        if new_coord in self.piece_coords:
            attacked_piece = self.piece_coords[new_coord]
            if self.is_wounded_on:
                self.wounded_coords[new_coord] = attacked_piece
            else:
                self.dead_pieces.append(attacked_piece)
        self.piece_coords[new_coord] = piece
        del self.piece_coords[old_coord]

    def draw_board_2d(self):
        self.draw_board(self.get_board_2d())

    def draw_board_2d_moves(self, moves):
        board = self.get_board_2d()
        for move in moves:
            board[self.size.y - move.y - 1][move.x] = " O "

        self.draw_board(board)

    def get_board_2d(self):
        board = [[" _ " for i in range(self.size.x)] for j in range(self.size.y)]
        for coord, piece in self.piece_coords.items():
            board[self.size.y - coord.y - 1][coord.x] = piece_mapping[piece.name]

        return board

    def draw_board(self, board):
        for row in board:
            print("".join(row))
        print("\n\n")
