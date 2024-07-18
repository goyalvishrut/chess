from model.Color import Color, toOppositeColor
from model.pieces.Bishop import Bishop
from model.pieces.King import King
from model.pieces.Knight import Knight
from model.pieces.Pawn import Pawn
from model.pieces.Piece import Piece
from model.pieces.Queen import Queen
from model.pieces.Rook import Rook


class Board:
    def __init__(self, player_name_1: str, player_name_2: str):
        white = Color.WHITE
        black = Color.BLACK
        self.__white_piece_player = player_name_1
        self.__black_piece_player = player_name_2

        self.__currentBoard: list[list[Rook | Knight | Bishop | Queen | King | Pawn | None]] = [
            [Rook(black), Knight(black), Bishop(black), Queen(black), King(black), Bishop(black), Knight(black),
             Rook(black)],
            [Pawn(black), Pawn(black), Pawn(black), Pawn(black), Pawn(black), Pawn(black), Pawn(black), Pawn(black)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(white), Pawn(white), Pawn(white), Pawn(white), Pawn(white), Pawn(white), Pawn(white), Pawn(white)],
            [Rook(white), Knight(white), Bishop(white), Queen(white), King(white), Bishop(white), Knight(white),
             Rook(white)],
        ]

        self.__currentPlayerChance = white

    def printCurrentBoard(self):
        iterations = len(self.__currentBoard)
        for r in range(iterations):
            for c in range(iterations):
                piece = self.__currentBoard[r][c]
                self.__printTopColHeader(r, c, iterations)
                self.__printStartRow(r, c)
                if piece is not None:
                    print(piece.symbol, end=" ")
                else:
                    print("--", end=" ")
                self.__printEndRow(r, c)
                self.__printBotColHeader(r, c, iterations)
            print('\n', end="")
        print()

    def movePiece(self, old: tuple[int, int], new: tuple[int, int]):
        try:
            if self.__validateMove(old, new):
                self.__movePiece(old, new)
            else:
                raise Exception("Invalid Move")
        except Exception as e:
            print(e.args)

    def __movePiece(self, old: tuple[int, int], new: tuple[int, int]):
        oldRow, oldCol = old
        newRow, newCol = new
        self.__currentBoard[newRow][newCol] = self.__currentBoard[oldRow][oldCol]
        self.__currentBoard[oldRow][oldCol] = None
        self.__currentPlayerChance = toOppositeColor(self.__currentPlayerChance)
        self.printCurrentBoard()

    def __validateMove(self, old: tuple[int, int], new: tuple[int, int]) -> bool:
        oldRow, oldCol = old
        newRow, newCol = new
        oldPlacePiece = self.__currentBoard[oldRow][oldCol]
        newPlacePiece = self.__currentBoard[newRow][newCol]
        return (oldPlacePiece is not None and
                oldPlacePiece.color is self.__currentPlayerChance and
                (newPlacePiece is None or newPlacePiece.color is not self.__currentPlayerChance) and
                oldPlacePiece.validate(oldRow, oldCol, newRow, newCol) and
                self.__validateJump(oldPlacePiece, old, new)
                )

    def __validateJump(self, pieceToMove: Piece, old: tuple[int, int], new: tuple[int, int]) -> bool:
        return True if pieceToMove is Knight else self.__isTrackEmpty(pieceToMove, old, new)

    def __isTrackEmpty(self, newPlacePiece: Piece, old: tuple[int, int], new: tuple[int, int]) -> bool:
        trackToCheck = newPlacePiece.getTrackToCheck(old[0], old[1], new[0], new[1])
        for r, c in trackToCheck:
            if self.__currentBoard[r][c] is not None:
                return False
        return True

    @staticmethod
    def __printCol(iterations: int):
        print(" ", end=" ")
        for i in range(iterations):
            print(chr(ord('a') + i), end="  ")

    def __printTopColHeader(self, r: int, c: int, iterations):
        if r == 0 and c == 0:
            self.__printCol(iterations)
            print()

    def __printBotColHeader(self, r: int, c: int, iterations):
        if r == 7 and c == 7:
            print()
            self.__printCol(iterations)

    @staticmethod
    def __printStartRow(r: int, c: int):
        if c == 0:
            print(r + 1, end=" ")

    @staticmethod
    def __printEndRow(r: int, c: int):
        if c == 7:
            print(r + 1, end=" ")
