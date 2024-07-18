from model.Color import Color
from model.pieces.Piece import Piece


class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(color, color.name[0] + 'N')

    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        return []

    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return (self.__validateUpTwoMove(oldRow, oldCol, newRow, newCol) or
                self.__validateUpDownMove(oldRow, oldCol, newRow, newCol) or
                self.__validateLeftTwoMove(oldRow, oldCol, newRow, newCol) or
                self.__validateRightTwoMove(oldRow, oldCol, newRow, newCol))

    @staticmethod
    def __validateUpTwoMove(oldRow, oldCol, newRow, newCol) -> bool:
        expectedNewRow = oldRow + 2
        expectedNewCol = [oldCol + 1, oldCol - 1]
        return (newRow == expectedNewRow) and (newCol in expectedNewCol)

    @staticmethod
    def __validateUpDownMove(oldRow, oldCol, newRow, newCol) -> bool:
        expectedNewRow = oldRow - 2
        expectedNewCol = [oldCol + 1, oldCol - 1]
        return (newRow == expectedNewRow) and (newCol in expectedNewCol)

    @staticmethod
    def __validateLeftTwoMove(oldRow, oldCol, newRow, newCol) -> bool:
        expectedNewCol = oldCol - 2
        expectedNewRow = [oldRow + 1, oldRow - 1]
        return (newCol == expectedNewCol) and (newRow in expectedNewRow)

    @staticmethod
    def __validateRightTwoMove(oldRow, oldCol, newRow, newCol) -> bool:
        expectedNewCol = oldCol + 2
        expectedNewRow = [oldRow + 1, oldRow - 1]
        return (newCol == expectedNewCol) and (newRow in expectedNewRow)
