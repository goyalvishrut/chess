import pygame

# Initialising pygame module
pygame.init()

# Setting Width and height of the Chess Game screen
WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Chess Game')

font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()
fps = 60
turn_step = 0


class PyGameGui:
    # draw main game board
    def drawBoard(self):
        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(screen, 'light gray', [
                    600 - (column * 200), row * 100, 100, 100])
            else:
                pygame.draw.rect(screen, 'light gray', [
                    700 - (column * 200), row * 100, 100, 100])
            pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
            pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
            pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
            status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                           'Black: Select a Piece to Move!', 'Black: Select a Destination!']
            screen.blit(big_font.render(
                status_text[turn_step], True, 'black'), (20, 820))
            for i in range(9):
                pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
                pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
            screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))


if __name__ == '__main__':
    while True:
        PyGameGui().drawBoard()
