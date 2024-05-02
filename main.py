import pygame, sys
from grid import Grid

pygame.init()

screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()

game_grid = Grid()
game_grid.grid[0][0] = 1
game_grid.print_grid()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(60)   

pygame.quit()