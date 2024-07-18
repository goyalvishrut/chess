class CliInput:

    def __init__(self):
        self.__validCol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def takeInput(self) -> tuple[tuple[int, int], tuple[int, int]]:
        return self.processInput(input(f'Input'))

    def processInput(self, move) -> tuple[tuple[int, int], tuple[int, int]]:
        try:
            if self.__shouldExit(move):
                exit(100)
            elif self.__isInputLengthValid(move) and self.__isInputFormatValid(move):
                moves = [move[0:2], move[3:5]]
                old = self.__getRowAndColFromInput(moves[0][1], moves[0][0])
                new = self.__getRowAndColFromInput(moves[1][1], moves[1][0])
                return old, new
            else:
                raise Exception('Invalid Input')
        except Exception as e:
            print(e.args[0])

    def __getRowAndColFromInput(self, row: str, col: str) -> tuple[int, int]:
        rowIndex = self.__getIndexForRow(row)
        colIndex = self.__getIndexForCol(col)
        return rowIndex, colIndex

    @staticmethod
    def __isInputLengthValid(move) -> bool:
        return len(move) == 5

    '''
    row -> int
    col -> str
    '''

    def __isInputFormatValid(self, move) -> bool:
        oldRow, oldCol, newRow, newCol, space = move[1:2], move[0:1], move[4:5], move[3:4], move[2:3]
        return (oldRow.isdigit() and oldCol.isalpha() and oldCol in self.__validCol and
                newRow.isdigit() and newCol.isalpha() and newCol in self.__validCol and
                space.isspace())

    @staticmethod
    def __shouldExit(move) -> bool:
        return move == 'exit'

    '''
    col -> str
    '''

    @staticmethod
    def __getIndexForCol(col: str) -> int:
        return ord(col) - ord('a')

    '''
    row -> int
    '''

    @staticmethod
    def __getIndexForRow(row: str) -> int:
        return 8 - int(row)
