from model.Color import Color
from model.pieces.Bishop import Bishop
from model.pieces.King import King
from model.pieces.Knight import Knight
from model.pieces.Pawn import Pawn
from model.pieces.Queen import Queen
from model.pieces.Rook import Rook

if __name__ == '__main__':
    rook = Rook(Color.WHITE)
    print(rook.validate(0, 2, 0, 4))
    rook = Bishop(Color.WHITE)
    print(rook.validate(0, 0, 5, 5))
    queen = Queen(Color.WHITE)
    print(queen.validate(0, 0, 5, 5))
    pawn = Pawn(Color.WHITE)
    print(pawn.validate(0, 0, 0, 1))
    king = King(Color.WHITE)
    print(king.validate(0, 0, 0, 1))
    knight = Knight(Color.WHITE)
    print(knight.validate(0, 0, 0, 1))
