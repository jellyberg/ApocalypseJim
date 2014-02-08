import pygame

pygame.init()

FPS = 60
FPSCLOCK = pygame.time.Clock()
WINDOWWIDTH = 1280
WINDOWHEIGHT = 480
HALFWINDOWWIDTH = int(WINDOWWIDTH / 2)
HALFWINDOWHEIGHT = int(WINDOWHEIGHT / 2)
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# Colours     R    G    B  ALPHA
WHITE     = (255, 255, 255, 255)
BLACK     = (  0,   0,   0, 255)
RED       = (255,   0,   0, 255)
DARKRED   = (220,   0,   0, 255)
BLUE      = (  0,   0, 255, 255)
SKYBLUE   = (135, 206, 250, 255)
YELLOW    = (255, 250,  17, 255)
GREEN     = (  0, 255,   0, 255)
ORANGE    = (255, 165,   0, 255)
DARKGREEN = (  0, 155,   0, 255)
DARKGREY  = ( 60,  60,  60, 255)
LIGHTGREY = (180, 180, 180, 255)
BROWN     = (139,  69,  19, 255)
CREAM     = (255, 255, 204, 255)

CELLSIZE = 20

PLAYERSPEED = 5