import pygame, sys
from grid import Grid

pygame.init()

screen = pygame.display.set_mode((300, 600))

clock = pygame.time.Clock()

player = pygame.Rect((0, 0, 50, 50))
game_grid = Grid()
game_grid.print_grid()

while True:

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

    player.move_ip(0, 1)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.display.update()
    clock.tick(60)
