from setting import *

class Score:
    def __init__(self):
        #placing the score surface ontop of the original surface
        # Game height and scoreboard need to have the same height, * the percentage we want it to take up, minus the padding
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.display_surface = pygame.display.get_surface()
    
    def run(self):
        #blit places one surface on top of another
        self.display_surface.blit(self.surface, (0,0))