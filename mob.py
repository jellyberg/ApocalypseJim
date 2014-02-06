import pygame, my, os
pygame.init()

class BasicSprite(pygame.sprite.Sprite):
    """A basic sprite that allows importing animations"""
    def __init__(self):
        self.animations = {}


    def loadImgs(self, filenameList, animNameList, directoryList, genFlippedAnims):
        """Loads animations into self.animations.
        filenameList[x] must correspond to animNameList[x] and directoryList[x]"""
        assert len(filenameList) == len(animNameList) == len(directoryList), "Must be an equal number of anims and names"
        if genFlippedAnims:
            originalAnimName = animName
            animName += 'L'
        for filename in filenameList:
            for animName in animNameList:
                for directory in directoryList:
                    anim = self.loadAnimationFiles(directory, filename)
                    self.animations{animName} = anim
                    if genFlippedAnims:
                        flippedAnim = self.flipAnimation(anim)
                        self.animations{originalAnimName += 'R'} = flippedAnim


    def loadAnimationFiles(directory, file):
        """Load images from directory into a list of surfaces"""
        animation = []
        frames = len(os.listdir(directory))
        for num in range(0, frames):
            num = str(num)
            num = num.zfill(4)
            img = pygame.image.load(directory + '/' + file +  '.' + num + '.png')
            animation.append(img)
        return animation


    def flipAnimation(self, animation):
        newAnimation = []
        for img in animation:
            pygame.transform.flip(img, True, False)
            newAnimation.append(img)
        return newAnimation



class GravSprite(pygame.sprite.Sprite):
    """A basic sprite which will obey gravity. Must be extended."""
    terminalVelocity = 10
    fallSpeed = 1
    def __init__(self, moveSpeed, jumpForce):
        self.moveSpeed, self.jumpForce = moveSpeed, jumpForce
        self.isOnGround = True
        self.move = None
        self.dir = 'right'
        self.xVel = 0
        self.yVel = 0


    def updatePos():
        """Updates the sprite's rect (x and y) based on its self.isOnGround and self.move"""
        # --Y VELOCITY--
        # FALL OR SLOW JUMPING IF IN THE AIR
        if not self.isOnGround:
            if self.yVel < gravSprite.terminalVelocity:
                self.yVel += gravSprite.fallSpeed
        # START JUMP
        elif self.isOnGround and self.startJump:
            self.yVel += self.jumpForce
            self.startJump == False
        # --X VELOCITY--
        if self.move == 'left': num = -1
        elif self.move == 'right': num = 1
        else: num = 0
        self.xVel += num
        self.rect.right += self.xVel
