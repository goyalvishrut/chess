from model.Color import Color
from model.pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, color: Color):
        super().__init__(color, color.name[0] + self.__class__.__name__[0])

    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        iteration = abs(oldRow - newRow) - 1
        if newRow < oldRow:
            if newCol < oldCol:
                return self.__getTopLeftMovingTrack(oldRow, oldCol, iteration)
            else:
                return self.__getTopRightMovingTrack(oldRow, oldCol, iteration)
        else:
            if newCol < oldCol:
                return self.__getDownLeftMovingTrack(oldRow, oldCol, iteration)
            else:
                return self.__getDownRightMovingTrack(oldRow, oldCol, iteration)

    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int, pieceAtNewPlace: Piece | None) -> bool:
        rowDiff = abs(oldRow - newRow)
        colDiff = abs(oldCol - newCol)
        return rowDiff == colDiff

    @staticmethod
    def __getTopLeftMovingTrack(oldRow: int, oldCol: int, iteration: int) -> list[tuple[int, int]]:
        track: list[tuple[int, int]] = []
        for i in range(iteration):
            track.append((oldRow - 1 - i, oldCol - 1 - i))
        return track

    @staticmethod
    def __getTopRightMovingTrack(oldRow: int, oldCol: int, iteration: int) -> list[tuple[int, int]]:
        track: list[tuple[int, int]] = []
        for i in range(iteration):
            track.append((oldRow - 1 - i, oldCol + 1 + i))
        return track

    @staticmethod
    def __getDownLeftMovingTrack(oldRow: int, oldCol: int, iteration: int) -> list[tuple[int, int]]:
        track: list[tuple[int, int]] = []
        for i in range(iteration):
            track.append((oldRow + 1 + i, oldCol - 1 - i))
        return track

    @staticmethod
    def __getDownRightMovingTrack(oldRow: int, oldCol: int, iteration: int) -> list[tuple[int, int]]:
        track: list[tuple[int, int]] = []
        for i in range(iteration):
            track.append((oldRow + 1 + i, oldCol + 1 + i))
        return track
