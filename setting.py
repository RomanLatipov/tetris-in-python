import pygame

#Game size
COLUMNS = 10
ROWS = 20
# how large a cell is, how wide and tall
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

#window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

#game behavior
UPDATE_START_SPEED = 800
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET =  pygame.Vector2(COLUMNS // 2, -1)

#color
BACKGROUND = '#113762'
LINE_WHITE = "#ffffff"
BLACK = "#000000"
PURPLE = '#07bac2'
YELLOW = '#db8514'
BLUE =  '#22b349'
ORANGE = '#d6c30c'
CYAN = '#6414db'
GREEN = '#d60ca9'
RED = "#9d0cd6"

#shapes
TETROMINOS = {
    "T" : { "shape": [(0,0), (-1,0), (1,0), (0,-1)], "color": PURPLE},
    "O" : { "shape": [(0,0), (0,-1), (1,0), (1,-1)], "color": YELLOW},
    "J" : { "shape": [(0,0), (0,-1), (0,1), (-1,1)], "color": BLUE},
    "L" : { "shape": [(0,0), (0,-1), (0,1), (1,1)], "color": ORANGE},
    "I" : { "shape": [(0,0), (0,-1), (0,-2), (0,1)], "color": CYAN},
    "S" : { "shape": [(0,0), (-1,0), (0,-1), (1,-1)], "color": GREEN},
    "Z" : { "shape": [(0,0), (1,0), (0, -1), (-1,-1)], "color": RED},
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}