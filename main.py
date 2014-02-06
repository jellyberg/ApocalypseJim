# APOCALYPSE JIM
# By Adam Binks

import pygame, sys, my, mob, player, level
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Apocalypse Jim')

loadingScreen = pygame.image.load('assets/loadingScreen.png').convert_alpha()
my.screen.blit(loadingScreen, (0, 0))
pygame.display.update()



def main():
    """Handle menu position"""
	runGame()


def runGame():
    """Run the actual game loop"""
    testMap = Level.Map('mapPack.txt')
    my.screen.blit(testMap.surf, (0,0))
    pygame.display.update()
    pygame.time.wait(2000)


def checkForQuit():
    """Terminate if QUIT events or K_ESCAPE"""
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def terminate():
    """Safely end the program"""
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()