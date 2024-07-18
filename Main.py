from model.Board import Board
from model.CliInput import CliInput


class Test:
    def __init__(self, gameBoard: Board, customInput: CliInput):
        self.board = gameBoard
        self.cli = customInput
        testInput: list[str] = ['e2 e4', 'e7 e5', 'f1 c4', 'b8 c6',
                                'd1 h5', 'g8 f6', 'h5 f7', 'f8 f7',
                                'g7 f7', 'h8 f7', 'd8 f7', 'c6 f7',
                                'c4 f7', 'h8 g8', 'f2 f4', 'e5 f4',
                                'f7 e8', 'exit']
        for i in testInput:
            old, new = customInput.processInput(i)
            gameBoard.movePiece(old, new)


if __name__ == '__main__':
    board = Board("1", "2")
    cli = CliInput()
    board.printCurrentBoard()
    while True:
        Test(board, cli)
        userInput = cli.takeInput()
        board.movePiece(userInput[0], userInput[1])
