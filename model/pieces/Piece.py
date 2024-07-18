from abc import ABC, abstractmethod
from model.Color import Color


class Piece(ABC):

    def __init__(self, color: Color):
        self.name = self.__class__.__name__
        self.color = color
        self.symbol = self.color.name[0] + self.__class__.__name__[0]
        # print("Piece created = ", self.name, "Piece color = ", self.pieceColor.name)

    def validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return self.__validateNewMove(newRow, newCol) and self._validate(oldRow, oldCol, newRow, newCol)

    @staticmethod
    def __validateNewMove(newRow: int, newCol: int) -> bool:
        result = 0 <= newRow < 8 and 0 <= newCol < 8
        if not result:
            print("Failed at base: Out of Board Move")
        return result

    @abstractmethod
    def _validate(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> bool:
        return False

    @abstractmethod
    def getTrackToCheck(self, oldRow: int, oldCol: int, newRow: int, newCol: int) -> list[tuple[int, int]]:
        return []
