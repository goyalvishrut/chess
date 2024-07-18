from model.pieces.Rook import Rook
from model.pieces.Bishop import Bishop


class Queen(Rook, Bishop):

    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        if self.__isRook(oldRow, oldCol, newRow, newCol):
            return Rook.getTrackToCheck(self, oldRow, oldCol, newRow, newCol)
        else:
            return Bishop.getTrackToCheck(self, oldRow, oldCol, newRow, newCol)

    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        # resultBishop = super(Rook, self)._validate(oldRow, oldCol, newRow, newCol)
        # resultRook = super()._validate(oldRow, oldCol, newRow, newCol)

        resultRook = self.__isRook(oldRow, oldCol, newRow, newCol)
        resultBishop = self.__isBishop(oldRow, oldCol, newRow, newCol)

        return resultBishop or resultRook

    def __isRook(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return Rook._validate(self, oldRow, oldCol, newRow, newCol)

    def __isBishop(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return Bishop._validate(self, oldRow, oldCol, newRow, newCol)
