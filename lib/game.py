from lib.settings import *
from lib.grid import Grid
from lib.blocks import *
from lib.preview import Preview
import random

class Game:
    def __init__(self, update_score):
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (padding, padding))
        self.update_score = update_score
        self.grid = Grid(update_score)
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.colors = colors()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.preview = Preview()

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.update_score(0, 1, 0, update_start_speed)

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def rotation(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            for i in range(4):
                column = self.current_block.get_cell_position()[i].column
                if column < 0:
                    self.current_block.move(0, abs(column))
                elif column > 9:
                    self.current_block.move(0, -1)
                row = self.current_block.get_cell_position()[i].row
                if row > 19:
                    self.current_block.move(19-row, 0)
    
    def lock_block(self):
        tiles = self.current_block.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_rows()
        if self.block_fits() == False:
            self.game_over = True

    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        for title in tiles:
            if self.grid.is_empty(title.row, title.column) == False:
                return False
        return True

    def run(self):
        self.display_surface.blit(self.surface, (padding, padding))
        self.surface.fill(self.colors[1])
        self.grid.draw(self.surface)
        pygame.draw.rect(self.display_surface, self.colors[2], self.rect, 2, 2)
        self.grid.draw(self.surface)
        self.current_block.draw(self.surface)