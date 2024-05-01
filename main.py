import pygame

# from setting, import everything
from setting import *
from sys import exit

#components
from game import Game

pygame.init()

screen = pygame.display.set_mode((1000, 600))

player = pygame.Rect((500, 250, 90, 50))

run = True
while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_UP] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

class Main:

    def __init__(self):
        pygame.init()
        #display laoyout
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

        self.game = Game()

    def run (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            #Background fill color
            self.display_surface.fill(GREEN)
            #Run the game.py settings
            self.game.run()

            pygame.display.update()
            self.clock.tick()

# to make sure we only run our setting and not anything else
if __name__ == '__main__':
    main = Main()
    main.run()