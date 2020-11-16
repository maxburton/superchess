from project.main.board import Board
from project.main.game import Game
from project.main.movement import Movement
from project.main.coord import Coord

from project.main.pieces.pawn import Pawn
from project.main.pieces.medic import Medic

if __name__ == "__main__":
    board = Board()
    game = Game()
    movement = Movement(board, game)

    pawn1 = Pawn("white")
    board.add_piece(pawn1, Coord(2, 1))

    medic1 = Medic("white")
    board.add_piece(medic1, Coord(4, 4))

    medic2 = Medic("black")
    board.add_piece(medic2, Coord(4, 5))

    medic3 = Medic("white")
    board.add_piece(medic2, Coord(5, 5))

    board.draw_board_2d()

    pawn1_moves = movement.get_available_moves(pawn1, Coord(2, 1))
    print(pawn1_moves)
    board.draw_board_2d_moves(pawn1_moves)

    medic1_moves = movement.get_available_moves(medic1, Coord(4, 4))
    print(medic1_moves)
    board.draw_board_2d_moves(medic1_moves)
