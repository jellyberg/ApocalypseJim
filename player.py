import pygame, mob, my
pygame.init()
from pygame.locals import *

animNameList  = ['run'                  ]
filenameList  = ['jimRun'               ]
directoryList = ['assets\player\jimRun']

moveSpeed = 3
jumpForce = 5

class Player(mob.GravSprite):
    """Player controlled Jim"""
    def __init__(self):
        mob.BasicSprite.__init__(self)
        mob.GravSprite.__init__(self, moveSpeed, jumpForce)
        self.loadImgs(filenameList, animNameList, directoryList, True)
        self.switchAnimation('runR')


    def update(self, *args):
        """Run all general update functions"""
        self.handleInput()
        self.updatePos()
        self.playAnimation()
        self.blit()


    def handleInput(self):
        self.move = None
        for key in my.input.pressedKeys:
            if key == K_RIGHT or key == K_d:
                self.move = 'right'
                if self.currentAnim != 'runR':
                    self.switchAnimation('runR')
            elif key == K_LEFT or key == K_a:
                self.move = 'left'
                if self.currentAnim != 'runL':
                    self.switchAnimation('runL')



def main():
    """For quick testing purposes"""
    testPlayer = Player()

if __name__ == '__main__':
    main()