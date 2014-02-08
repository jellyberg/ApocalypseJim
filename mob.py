import pygame, my, os, random
pygame.init()

class BasicSprite(pygame.sprite.Sprite):
    """A basic sprite that allows importing animations"""
    def __init__(self):
        self.animations = {}


    def loadImgs(self, filenameList, animNameList, directoryList, genFlippedAnims):
        """Loads animations into self.animations.
        filenameList[x] must correspond to animNameList[x] and directoryList[x]"""
        assert len(filenameList) == len(animNameList) == len(directoryList), "Must be an equal number of anims and names"
        for filename in filenameList:
            for animName in animNameList:
                # SET UP RIGHT/LEFT ANIMNAMES
                if genFlippedAnims:
                    originalAnimName = animName
                    animName += 'R'
                for directory in directoryList:
                    # IMPORT ANIMATION FILES
                    anim = self.loadAnimationFiles(directory, filename)
                    self.animations[animName] = anim
                    if genFlippedAnims:
                        flippedAnim = self.flipAnimation(anim)
                        flippedName = originalAnimName + 'L'
                        self.animations[flippedName] = flippedAnim
        # PICK FIRST IMAGE FROM A RANDOM ANIMATION TO GENERATE SELF.RECT
        self.surf = self.animations[random.choice(list(self.animations.keys()))][0]
        self.rect = self.surf.get_rect()
        self.gameRect = self.rect.copy()


    def loadAnimationFiles(self, directory, file):
        """Load images from directory into a list of surfaces"""
        animation = []
        frames = len(os.listdir(directory))
        for num in range(0, frames):
            num = str(num)
            num = num.zfill(4)
            img = pygame.image.load(directory + '/' + file +  '.' + num + '.png').convert_alpha()
            animation.append(img)
        return animation


    def flipAnimation(self, animation):
        """Simply horizontally flip each surface in the given list of surfaces"""
        newAnimation = []
        for img in animation:
            img = pygame.transform.flip(img, True, False)
            newAnimation.append(img)
        return newAnimation


    def playAnimation(self):
        """Update self.surf with next animation frame"""
        assert self.currentAnim, "No animation playing!"
        self.surf = self.animations[self.currentAnim][self.animFrame]
        self.animFrame += 1
        if self.animFrame > len(self.animations[self.currentAnim]) - 1:
            self.animFrame = 0


    def switchAnimation(self, animName):
        """Switch to a different animation cycle"""
        self.currentAnim = animName
        self.animFrame = 0


    def blit(self):
        """Blit to screen. Duh."""
        my.masterSurf.blit(self.surf, self.gameRect)


    def getMapArea(self):
        """Returns a list of map coords that the given rect overlaps"""
        rect = self.gameRect
        mapArea = []
        topLeftx, topLefty = self.pixelsToMap(rect.topleft)
        bottomRightx, bottomRighty = self.pixelsToMap(rect.bottomright)
        for x in range(topLeftx, bottomRightx):
            for y in range(topLefty, bottomRighty):
                mapArea.append([x, y])
        return mapArea


    def pixelsToMap(self, pixels):
        """Returns map coords when given my.masterSurf pixel coords"""
        x, y = pixels
        return int(x / my.CELLSIZE), int(y / my.CELLSIZE) 




class GravSprite(BasicSprite):
    """A basic sprite which will obey gravity. Must be extended."""
    terminalVelocity = 10
    fallSpeed = 1
    def __init__(self, moveSpeed, jumpForce):
        self.moveSpeed, self.jumpForce = moveSpeed, jumpForce
        self.isOnGround = True
        self.tryToJump = False
        self.move = None
        self.dir = 'right'
        self.xVel = 0
        self.yVel = 0


    def updatePos(self):
        """Updates the sprite's gameRect (x and y) based on its self.isOnGround and self.move"""
        self.isOnGround = self.getIsOnGround()
        # --Y VELOCITY--
        # FALL OR SLOW JUMPING IF IN THE AIR
        if not self.isOnGround:
            if self.yVel < gravSprite.terminalVelocity:
                self.yVel += gravSprite.fallSpeed
        # START JUMP
        elif self.isOnGround and self.tryToJump:
            self.yVel += self.jumpForce
            self.tryToJump == False
        elif self.isOnGround:
            self.yVel = 0
        # --X VELOCITY--
        self.xVel = 0
        if self.move == 'left':
            num = -1 * self.moveSpeed
            self.dir = 'left'
        elif self.move == 'right':
            num = 1 * self.moveSpeed
            self.dir = 'right'
        else: num = 0
        self.xVel += num
        self.gameRect.right += self.xVel


    def getIsOnGround(self):
        x, y = 0, 1
        area = self.getMapArea()
        for coord in area:
            if coord[y + 1] > my.map.yCellNum or my.map.isSolid(coord[x], coord[y + 1]):
                return True
        return False
        



def main():
    """For quick testing purposes"""
    pass

if __name__ == '__main__':
    main()