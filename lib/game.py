from setting import *

class Game:
    def __init__(self):
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        #blit places one surface on top of another
        self.display_surface.blit(self.surface, (PADDING,PADDING))