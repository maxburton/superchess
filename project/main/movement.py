class Movement:
    def __init__(self, board, game):
        self.board = board
        self.game = game

        self.keywords = {
            "normal": self.is_valid,
            "first": self.is_first_move,
            "attack": self.is_attacking,
            "carrying": self.is_carrying
        }

    def get_available_moves(self, piece, pos, get_relative_move=True):
        available_moves = set()
        for coord, keywords in piece.movement.items():
            for keyword in keywords:
                if self.keywords[keyword](piece=piece, new_pos=pos.add(coord)):
                    if get_relative_move:
                        available_moves.add(coord.add(pos))
                    else:
                        available_moves.add(coord)
        return list(available_moves)

    def move(self, piece=None, old_pos=None, new_pos=None):
        for keyword in piece.movement[new_pos]:
            if self.check_move(keyword, piece=piece, new_pos=new_pos):
                # Move the piece
                piece = self.board.piece_coords.pop(old_pos, None)
                if self.is_attacking(piece=piece, new_pos=new_pos):
                    killed_piece = self.board.piece_coords.pop(new_pos, None)
                    self.board.dead_pieces.append(killed_piece)
                self.board.piece_coords[new_pos] = piece

            else:
                print("Illegal move!")

    def check_move(self, keyword, piece=None, new_pos=None):
        return self.keywords[keyword](piece=piece, new_pos=new_pos) and self.is_valid(piece=piece, new_pos=new_pos)

    def normal_move(self, **kwargs):
        return True

    def is_inbounds(self, new_pos):
        return 0 <= new_pos.x <= self.board.size.x and 0 <= new_pos.y <= self.board.size.y

    def is_valid(self, piece=None, new_pos=None):
        return self.is_inbounds(new_pos) and self.is_not_attacking_team(piece, new_pos)

    def is_first_move(self, piece=None, **kwargs):
        return piece.is_first_move

    def does_piece_exist_in_new_pos(self, new_pos=None):
        return self.board.get_from_coord(new_pos)

    def is_not_attacking_team(self, piece, new_pos):
        attacking_piece = self.does_piece_exist_in_new_pos(new_pos=new_pos)
        if attacking_piece:
            if piece.can_attack:
                return self.is_attacking_different_team(piece, attacking_piece)
            return False
        return True

    def is_attacking_different_team(self, piece, attacking_piece):
        for team in self.game.teams:
            if piece.colour in team and attacking_piece.colour in team:
                return False
        return True

    def is_attacking(self, piece=None, new_pos=None, **kwargs):
        attacking_piece = self.does_piece_exist_in_new_pos(new_pos=new_pos)
        if attacking_piece:
            return self.is_attacking_different_team(piece, attacking_piece)
        return False

    def is_carrying(self, piece=None, **kwargs):
        return piece.is_carrying
