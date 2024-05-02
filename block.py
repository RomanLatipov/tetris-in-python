import pygame
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 40
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == 4:
            self.rotation_state = 0

    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def draw(self, screen):
        tiles = self.get_cell_position()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size+1, tile.row * self.cell_size+1, self.cell_size-1, self.cell_size - 1)
            color = ((255,0,0))
            if self.id == 2:
                color = (0, 34, 255)
            pygame.draw.rect(screen, color, tile_rect)

class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column