from model.pieces.Piece import Piece


class King(Piece):
    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        return []

    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return self.__validateKing(oldRow, oldCol, newRow, newCol)

    @staticmethod
    def __validateKing(oldRow, oldCol, newRow, newCol):
        return ((abs(newCol - oldCol) == 1 and newRow == oldRow) or
                (abs(newRow - oldRow) == 1 and newCol == oldCol))
