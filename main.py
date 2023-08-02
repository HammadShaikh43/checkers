import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BOOT
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def ai():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)
            
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

def aiVai():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)
        pygame.time.delay(150)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)
        else:
            value, new_board = minimax(game.get_board(), 4, RED, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        game.update()
        
def pvp():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        
def start_screen():
        pygame.init()
        display_surface = pygame.display.set_mode((WIDTH, HEIGHT ))
        while True :
        
            smallfont = pygame.font.SysFont('Typori',35) 
            text = smallfont.render('Player vs AI' , True , (121,199,139))
            text2 = smallfont.render('Player vs Player' , True , (121,199,139))
            text3 = smallfont.render('AI vs AI' , True , (121,199,139))            
            text4 = smallfont.render('Quit' , True , (121,199,139))
            
            for ev in pygame.event.get():
                
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    
                    if WIDTH/4 <= mouse[0] <= WIDTH/4+300 and HEIGHT/4 <= mouse[1] <= HEIGHT/4+40:
                        ai()
                        pygame.quit()
                    if WIDTH/3 <= mouse[0] <= WIDTH/3+300 and HEIGHT/3 <= mouse[1] <= HEIGHT/3+40:
                        pvp()
                        pygame.quit()
                    if WIDTH/2 <= mouse[0] <= WIDTH/2+300 and HEIGHT/2-70 <= mouse[1] <= HEIGHT/2:
                        aiVai()
                        pygame.quit()
                    if WIDTH/4 <= mouse[0] <= WIDTH/4+300 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                        pygame.quit()

            display_surface.fill(WHITE)
        

            display_surface.blit(BOOT, (0, 0))
            
            mouse = pygame.mouse.get_pos()
            # for player v ai

            if WIDTH/4 <= mouse[0] <= WIDTH/4+300 and HEIGHT/4 <= mouse[1] <= HEIGHT/4+40:
                pygame.draw.rect(display_surface,(255,255,255),[WIDTH/4,HEIGHT/4,280,40])
                
            else:
                pygame.draw.rect(display_surface,(0,0,0),[WIDTH/4,HEIGHT/4,300,40])
            
            display_surface.blit(text , (WIDTH/4+5,HEIGHT/4))
            # for pvp
            
            if WIDTH/3 <= mouse[0] <= WIDTH/3+300 and HEIGHT/3 <= mouse[1] <= HEIGHT/3+40:
                pygame.draw.rect(display_surface,(255,255,255),[WIDTH/3,HEIGHT/3,300,40])
                
            else:
                pygame.draw.rect(display_surface,(0,0,0),[WIDTH/3,HEIGHT/3,300,40])

            display_surface.blit(text2 , (WIDTH/3+5,HEIGHT/3))
            
            #for aiVai
            
            if WIDTH/2 <= mouse[0] <= WIDTH/2+300 and HEIGHT/2-70 <= mouse[1] <= HEIGHT/2:
                pygame.draw.rect(display_surface,(255,255,255),[WIDTH/2,HEIGHT/2-70,300,40])
                
            else:
                pygame.draw.rect(display_surface,(0,0,0),[WIDTH/2,HEIGHT/2-70,300,40])

            display_surface.blit(text3 , (WIDTH/2+5,HEIGHT/2-70))
            
            # for Quit
            
            if WIDTH/4 <= mouse[0] <= WIDTH/4+300 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                pygame.draw.rect(display_surface,(255,255,255),[WIDTH/4,HEIGHT/2,300,40])
                
            else:
                pygame.draw.rect(display_surface,(0,0,0),[WIDTH/4,HEIGHT/2,300,40])

            display_surface.blit(text4 , (WIDTH/4+5,HEIGHT/2))

            pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    start_screen()
  
    pygame.quit()

main()