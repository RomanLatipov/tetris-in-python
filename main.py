from lib.settings import *
from sys import exit
from lib.game import Game
from lib.preview import Preview
from lib.score import Score

def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    game_update = pygame.USEREVENT
    pygame.time.set_timer(game_update, 500)
    preview = Preview()
    score = Score()
    
    def update_score(lines, score, level):
        score.lines = lines
        score.score = score
        score.level = level
        
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == game_update and game.game_over == False:
                game.move_down()
            if game.game_over == True:
                game.game_over = False
                game.reset()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] == True and game.game_over == False:
            game.move_left()
        elif key[pygame.K_RIGHT] == True and game.game_over == False:
            game.move_right()
        elif key[pygame.K_DOWN] == True and game.game_over == False:
            game.move_down()
        elif key[pygame.K_UP] == True and game.game_over == False:
            game.rotation()
                
        screen.fill(colors()[0])
        game.run()
        preview.run()
        score.run()
       
        pygame.display.update()
        clock.tick(12)
    
if __name__ == '__main__':
    main()