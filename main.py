import sys
import pygame
from pygame.locals import *
from numpy import matrix

# TODO add index checks in your moveL/R/D functions
# TODO generate pieces

# Helper functions ------------------------------------------------------#
def printMatrix(matrix):
    for row in range(len(matrix)):
        print matrix[row]
#------------------------------------------------------------------------#

# Drawing functions -----------------------------------------------------#
def drawGame(surface, grid):
    # grid[row][col]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                pygame.draw.rect(surface, WHITE, (CELL_W*col, CELL_H*row, CELL_W, CELL_H))

# TODO Abstract away from drawing pieces -- pieces should be matrices?
def drawIBlock(surface, color, x, y):
    pygame.draw.rect(surface, color, (x, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x, y+CELL_H, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x, y+2*CELL_H, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x, y+3*CELL_H, CELL_W, CELL_H))
def drawOBlock(surface, color, x, y):
    pygame.draw.rect(surface, color, (x, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+CELL_W, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x, y+CELL_H, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+CELL_W, y+CELL_H, CELL_W, CELL_H))
def drawZBlock(surface, color, x, y):
    pygame.draw.rect(surface, color, (x, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+CELL_W, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+CELL_W, y+CELL_H, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+2*CELL_W, y+CELL_H, CELL_W, CELL_H))
def drawTBlock(surface, color, x, y):
    pygame.draw.rect(surface, color, (x, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+CELL_W, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+2*CELL_W, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+CELL_W, y+CELL_H, CELL_W, CELL_H))
def drawLBlock(surface, color, x, y):
    pygame.draw.rect(surface, color, (x, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x, y+CELL_H, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+CELL_W, y, CELL_W, CELL_H))
    pygame.draw.rect(surface, color, (x+2*CELL_W, y, CELL_W, CELL_H))
#------------------------------------------------------------------------#

# Matrix manipulation ---------------------------------------------------#
def moveLeft(piece):
    foo = [[0]*10 for i in range(20)]
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == 1:
                foo[row][col-1] = 1
    return foo
def moveRight(piece):
    foo = [[0]*10 for i in range(20)]
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == 1:
                foo[row][col+1] = 1
    return foo
def moveDown(piece):
    foo = [[0]*10 for i in range(20)]
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == 1:
                foo[row+1][col] = 1
    return foo

def mergeGamePiece(game, piece):
    foo = [[0]*10 for i in range(20)]
    for row in range(len(game)):
        for col in range(len(game[row])):
            if (game[row][col] == 1) and (piece[row][col] == 1):
                return None
            else:
                foo[row][col] = game[row][col] + piece[row][col]
    return foo

#------------------------------------------------------------------------#

# Initialise the game engine
pygame.init()

# Window size
WIDTH, HEIGHT = 200, 400
CELL_W, CELL_H = WIDTH/10, HEIGHT/20
W_SIZE   = (WIDTH, HEIGHT)
W_CENTER = (WIDTH/2, HEIGHT/2)

# Usual colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# Create window
screen = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption("Tetris")
# background = pygame.image.load('game.png').convert()

# Create clock
clock = pygame.time.Clock()
game = [[0]*10 for i in range(20)]
piece = [[0]*10 for i in range(20)]
piece[1][1] = 1
piece[2][1] = 1
piece[3][1] = 1
piece[4][1] = 1
# printMatrix(piece)

# Loop until quit
while True:
    # Lock the game at 50fps
    clock.tick(50)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    gp = mergeGamePiece(game, piece)

    # Check input
    if (event.type == KEYUP) or (event.type == KEYDOWN):
        if event.key == pygame.K_LEFT:
            piece = moveLeft(piece)
        elif event.key == pygame.K_RIGHT:
            piece = moveRight(piece)
        elif event.key == pygame.K_DOWN:
            piece = moveDown(piece)
        # elif event.key == pygame.K_UP:
        #

    if not(mergeGamePiece(game, piece) is None):
        gp = mergeGamePiece(game, piece)

    drawGame(screen, gp)

    # Move objects...

    # Draw objects...
    # screen.blit(background, (100,100))

    # Update the screen
    pygame.display.flip()


