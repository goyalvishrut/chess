from model.Color import Color
from model.pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(color, color.name[0] + self.__class__.__name__[0])

    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        return (self.__getTrackForWhite(oldRow, oldCol, newCol) if self.color == Color.WHITE
                else self.__getTrackForBlack(oldRow, oldCol, newCol))

    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int, pieceAtNewPlace: Piece | None) -> bool:
        result = (self.validateWhitePawn(oldRow, newRow, ) if self.color == Color.WHITE
                  else self.validateBlackPawn(oldRow, newRow))
        if newCol != oldCol and abs(newCol - oldCol) == 1:
            return result and pieceAtNewPlace is not None
        else:
            return newCol == oldCol and pieceAtNewPlace is None

    @staticmethod
    def validateWhitePawn(oldRow: int, newRow: int, ) -> bool:
        validDiff: list[int] = [-1]
        if oldRow == 6:
            validDiff.append(-2)
        return (newRow - oldRow) in validDiff

    @staticmethod
    def validateBlackPawn(oldRow: int, newRow: int, ) -> bool:
        validDiff: list[int] = [1]
        if oldRow == 1:
            validDiff.append(2)
        return (newRow - oldRow) in validDiff

    @staticmethod
    def __getTrackForWhite(oldRow: int, oldCol: int, newCol: int) -> list[tuple[int, int]]:
        if oldCol == newCol:
            return [(oldRow - 1, oldCol)]
        else:
            return []

    @staticmethod
    def __getTrackForBlack(oldRow: int, oldCol: int, newCol: int) -> list[tuple[int, int]]:
        if oldCol == newCol:
            return [(oldRow + 1, oldCol)]
        else:
            return []
