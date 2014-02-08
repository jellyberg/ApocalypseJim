# APOCALYPSE JIM
# By Adam Binks
# 01/02/14

import pygame, my, mob, player, level, input
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Apocalypse Jim')

loadingScreen = pygame.image.load('assets/loadingScreen.png').convert_alpha()
my.screen.blit(loadingScreen, (0, 0))
pygame.display.update()



def main():
    """Handle menu position"""
    my.screen.fill(my.RED)
    my.input = input.Input()
    runGame()


def runGame():
    """Run the actual game loop"""
    my.map = level.Map('mapPack.txt')
    my.player = player.Player()
    my.camera = level.Camera()
    my.masterSurf = my.map.surf.copy()

    while True: # MAIN GAME LOOP
        my.input.get()
        my.masterSurf.blit(my.map.surf, (0,0))
        my.player.update()
        my.camera.update()
        pygame.display.update()
        my.FPSCLOCK.tick(my.FPS)
        my.input.checkForQuit()



if __name__ == '__main__':
    main()