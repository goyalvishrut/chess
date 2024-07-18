from model.Color import Color
from model.pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(color, color.name[0] + self.__class__.__name__[0])

    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        return (self.__getTrackForWhite(oldRow, oldCol) if self.color == Color.WHITE
                else self.__getTrackForBlack(oldRow, oldCol))

    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return (self.validateWhitePawn(oldRow, oldCol, newRow, newCol) if self.color == Color.WHITE
                else self.validateBlackPawn(oldRow, oldCol, newRow, newCol))

    @staticmethod
    def validateWhitePawn(oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        validDiff: list[int] = [-1]
        if oldRow == 6:
            validDiff.append(-2)
        return newCol == oldCol and (newRow - oldRow) in validDiff

    @staticmethod
    def validateBlackPawn(oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        validDiff: list[int] = [1]
        if oldRow == 1:
            validDiff.append(2)
        return newCol == oldCol and (newRow - oldRow) in validDiff

    @staticmethod
    def __getTrackForWhite(oldRow: int, oldCol: int) -> list[tuple[int, int]]:
        return [(oldRow - 1, oldCol)]

    @staticmethod
    def __getTrackForBlack(oldRow: int, oldCol: int) -> list[tuple[int, int]]:
        return [(oldRow + 1, oldCol)]
