import pygame
from play_game import Game

pygame.init()

screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()
game = Game()
game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 500)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == game_update:
            game.move_down()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        game.move_left()
    elif key[pygame.K_RIGHT] == True:
        game.move_right()
    elif key[pygame.K_DOWN] == True:
        game.move_down()
    elif key[pygame.K_UP] == True:
        game.rotation()
    
    
    screen.fill((255, 255, 255))
    game.draw(screen)

    pygame.display.update()
    clock.tick(15)   

pygame.quit()