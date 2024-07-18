from model.Color import Color
from model.pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, color: Color):
        super().__init__(color, color.name[0] + self.__class__.__name__[0])

    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        return (self.__trackForRow(oldRow, newRow, oldCol) if (oldCol == newCol)
                else self.__trackForCol(oldCol, newCol, oldRow))

    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return ((oldCol == newCol) and (oldRow != newRow)) or ((oldCol != newCol) and (oldRow == newRow))

    @staticmethod
    def __trackForRow(oldRow: int, newRow: int, col: int) -> list[tuple[int, int]]:
        track: list[tuple[int, int]] = []
        if newRow > oldRow:
            for i in range(newRow - oldRow - 1):
                track.append((oldRow + i + 1, col))
        else:
            for i in range(oldRow - newRow + 1):
                track.append((oldRow - i - 1, col))
        return track

    @staticmethod
    def __trackForCol(oldCol: int, newCol: int, row: int) -> list[tuple[int, int]]:
        track: list[tuple[int, int]] = []
        if newCol > oldCol:
            for i in range(newCol - oldCol - 1):
                track.append((row, oldCol + i + 1))
        else:
            for i in range(oldCol - newCol + 1):
                track.append((row, oldCol - i - 1))
        return track
