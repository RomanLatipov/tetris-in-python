from os.path import join
from lib.settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((sidebar_width, game_height * 0.3 - padding))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(bottomright = (window_width - padding, window_height - padding))

        self.font = pygame.font.Font(join('.', 'graphics', 'Russo_One.ttf'),30)
        self.increment_height = self.surface.get_height() / 3

        self.colors = colors()

    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, 'white')
        text_rext = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface, text_rext)
                
    def run(self, score, level, lines):
        self.surface.fill(self.colors[0])
        for i, text in enumerate([('Score', score), ('Level', level), ('Lines', lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x,y), text)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, self.colors[9], self.rect, 2, 2)