import sys
import pygame
from pygame.locals import *
from numpy import matrix

def drawGame(surface, grid):
    # grid[row][col]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col][0] == 1:
                pygame.draw.rect(surface, grid[row][col][1], (CELL_W*col, CELL_H*row, CELL_W, CELL_H))
                # print "(" + str(row) + ", " + str(col) + ")"

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
    
def printMatrix(matrix):
    for row in range(len(matrix)):
        print matrix[row]

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
# background = pygame.image.load('game.png').convert()
pygame.display.set_caption("Tetris")

# Create clock
clock = pygame.time.Clock()

piece = [[0]*10 for i in range(20)]
piece[1][1] = 1
piece[2][1] = 1
piece[3][1] = 1
piece[4][1] = 1
printMatrix(piece)
print ""
printMatrix(moveDown(piece))
        # for col in range(len(grid[row])):
        #     if grid[row][col][0] == 1:
        #         pygame.draw.rect(surface, grid[row][col][1], (CELL_W*col, CELL_H*row, CELL_W, CELL_H))
# print piece

# Loop until quit
# while True:
#     # Lock the game at 50fps
#     clock.tick(50)

#     # Process events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

#     # Clear the screen
#     screen.fill(BLACK)

#     # Check input

#     # Move objects...

#     # Draw objects...
#     grid = [[(0, BLACK)]*10 for i in range(20)]
#     grid[19][9] = (1, BLUE)
#     drawGame(screen, grid)

#     # screen.blit(background, (100,100))
#     # drawIBlock(screen, BLUE, 0, 0)
#     # drawOBlock(screen, RED, 0, 0)
#     # drawZBlock(screen, WHITE, 0, 0)
#     # drawTBlock(screen, GREEN, 0, 0)
#     # drawLBlock(screen, RED, 0, 0)

#     # Update the screen
#     pygame.display.flip()



