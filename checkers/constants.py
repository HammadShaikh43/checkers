import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# rgb
RED = (42, 100, 101)
WHITE = (176.25, 54, 28.5)
BLACK = (0, 0, 0)
BLUE = (255, 255, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
BOOT = pygame.transform.scale(pygame.image.load('assets/BACKGROUND.jpg'), (800, 800))

