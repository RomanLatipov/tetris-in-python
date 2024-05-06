from lib.settings import *
import random
from lib.score import Score
from lib.preview import Preview

class Game:
    def __init__(self):
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()
        self.preview = Preview()
        self.score = Score()
    
    def run(self):
        self.display_surface.blit(self.surface, (padding, padding))
        self.preview.run()
        self.score.run()
        self.draw_grid()

    def draw_grid(self):
        for col in range(1, columns):
            x = col * cell_size
            pygame.draw.line(self.surface, white, (x, 0), (x, self.surface.get_height()), 1)

        for row in range(1, rows):
            y = row * cell_size
            pygame.draw.line(self.surface, white, (0, y), (self.surface.get_width(),y))
        
        self.surface.blit(self.surface, (0, 0))

        # for row in range(rows):
        #     for column in range(columns):
        #         cell_rect = pygame.Rect(column*cell_size, row*cell_size, cell_size-1, cell_size-1)
        #         pygame.draw.rect(self.surface, blue, cell_rect)