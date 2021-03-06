import pygame, os, random, my
pygame.init()


class Map:
	"""Access to functions relating to the map"""
	dirtImg = pygame.image.load('assets/dirt.png')
	dirtImg = pygame.transform.scale(dirtImg, (my.CELLSIZE, my.CELLSIZE))

	def __init__(self, filename):
		levelsList = readLevelFiles(filename)
		self.allData = self.genDataStructure(levelsList)
		self.mapNum = random.randint(0, len(self.allData) - 1)
		self.map = self.allData[self.mapNum]
		self.genSurf()
		self.width = self.surf.get_width()
		self.xCellNum, self.yCellNum = len(self.map), len(self.map[0])


	def genDataStructure(self, strList):
		"""Returns data, a list of levels, which are lists of lists of what's gan on in each tile"""
		data = []
		for levelNum in range(len(strList)):
			level = []
			for x in range(len(strList[levelNum])):
				level.append([])
				for y in range(len(strList[levelNum][x])):
					level[x].append(strList[levelNum][x][y])
			data.append(level)
		return data


	def isSolid(self, x, y):
		"""Look at the function name. Duh."""
		if self.map[x][y] != ' ':
			return True
		return False


	def genSurf(self):
		"""Generates a base surf for the entire map, stored as self.surf"""
		self.surf = pygame.Surface((len(self.map) * my.CELLSIZE, len(self.map[0]) * my.CELLSIZE))
		self.surf.fill(my.BLUE)
		for x in range(len(self.map)):
			for y in range(len(self.map[0])):
				if self.map[x][y] == 'G':
					self.surf.blit(Map.dirtImg, (x * my.CELLSIZE, y * my.CELLSIZE))
		self.surf = pygame.transform.rotate(self.surf, 270)
		self.surf = pygame.transform.flip(self.surf, True, False)



class Camera:
	"""Allows for a scrolling game view, and camera shake."""
	def __init__(self):
		self.gameRect = pygame.Rect(0, 0, my.WINDOWWIDTH, my.WINDOWHEIGHT)
		self.gameRect.centerx = my.player.gameRect.centerx
		self.width = my.WINDOWWIDTH
		self.shake = 0

	def update(self):
		"""Updates camera pos and shake, and blits the to my.screen"""
		self.gameRect.centerx = my.player.gameRect.centerx
		if self.gameRect.left < 0: self.gameRect.left = 0
		elif self.gameRect.right > my.map.width: self.gameRect.right = my.map.width
		my.screen.blit(my.masterSurf, (0,0), self.gameRect)


def readLevelFiles(filename):
	"""Creates a list of strings which constitute the levels in the given 'filename' map pack"""
	assert os.path.exists(filename), 'Cannot read level file ' + filename
	mapFile = open(filename, 'r')
	content = mapFile.readlines() + ['\r\n']
	mapFile.close()

	levels = []
	levelNum = 0
	levelTextLines = []
	mapObj = []

	# GENERATE MAPTEXTLINES
	for lineNum in range(len(content)):
		# PROCESS EACH LINE
		line = content[lineNum].rstrip('\r\n')# remove /n from the end of each line
		line = line.rstrip('.')
		if '/' in line: # end of level
			levels.append(levelTextLines)
			levelTextLines = []
			continue
		elif '#' in line: # its a comment
			continue
		elif '/' not in line and '#' not in line: # its part of the map
			levelTextLines.append(line) # so add it to it
	return levels

	
def main():
	"""For quick testing purposes"""
	pass

if __name__ == '__main__':
    main()