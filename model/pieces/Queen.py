from model.Color import Color
from model.pieces.Bishop import Bishop
from model.pieces.Piece import Piece
from model.pieces.Rook import Rook


class Queen(Rook, Bishop):
    def __init__(self, color: Color):
        Piece.__init__(self, color, color.name[0] + self.__class__.__name__[0])

    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        if self.__isRook(oldRow, oldCol, newRow, newCol):
            return Rook.getTrackToCheck(self, oldRow, oldCol, newRow, newCol)
        else:
            return Bishop.getTrackToCheck(self, oldRow, oldCol, newRow, newCol)

    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int, pieceAtNewPlace: Piece | None) -> bool:
        # resultBishop = super(Rook, self)._validate(oldRow, oldCol, newRow, newCol)
        # resultRook = super()._validate(oldRow, oldCol, newRow, newCol)

        resultRook = self.__isRook(oldRow, oldCol, newRow, newCol)
        resultBishop = self.__isBishop(oldRow, oldCol, newRow, newCol)

        return resultBishop or resultRook

    def __isRook(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return Rook._validate(self, oldRow, oldCol, newRow, newCol, None)

    def __isBishop(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return Bishop._validate(self, oldRow, oldCol, newRow, newCol, None)
