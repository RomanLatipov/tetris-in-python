from lib.settings import *
from sys import exit
from lib.game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.fill(background)
        game.run()
       
        pygame.display.update()
        clock.tick()

    
if __name__ == '__main__':
    main()