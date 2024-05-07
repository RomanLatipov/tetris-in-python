import pygame

columns = 10
rows = 20
cell_size = 40
game_width = columns * cell_size
game_height = rows * cell_size

sidebar_width = 200
preview_height_fraction = 0.7
score_height_fraction = 0.3

#window
padding = 20
window_width = game_width + sidebar_width + padding * 3
window_height = game_height + padding * 2

#game behavior
update_start_speed = 800
move_wait_time = 200
rotate_wait_time = 200
block_offset =  pygame.Vector2(columns // 2, -1)

#color
def colors():
    background = '#3b3b3b'
    grey = '#8c8c8c'
    white = "#ffffff"
    black = "#000000"
    purple = '#8b43cc'
    yellow = '#e8d915'
    blue =  '#155be8'
    orange = '#e89915'
    cyan = '#43b4a4'
    green = '#1fd118'
    red = "#d11836"

    return [background, grey, white, black, green, red, orange, yellow, purple, cyan, blue]

#shapes
tetrominos = {
    "t" : { "shape": [(0,0), (-1,0), (1,0), (0,-1)], "color": colors()[8]},
    "o" : { "shape": [(0,0), (0,-1), (1,0), (1,-1)], "color": colors()[7]},
    "j" : { "shape": [(0,0), (0,-1), (0,1), (-1,1)], "color": colors()[10]},
    "l" : { "shape": [(0,0), (0,-1), (0,1), (1,1)], "color": colors()[6]},
    "i" : { "shape": [(0,0), (0,-1), (0,-2), (0,1)], "color": colors()[9]},
    "s" : { "shape": [(0,0), (-1,0), (0,-1), (1,-1)], "color": colors()[4]},
    "z" : { "shape": [(0,0), (1,0), (0, -1), (-1,-1)], "color": colors()[5]},
}

score_data = {1: 40, 2: 100, 3: 300, 4: 1200}