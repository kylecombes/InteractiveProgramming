"""Ice Cream Game Code"""


import pygame
import time
import random
from helpers import *
from pygame.locals import *
from ice_cream_cone import IceCreamCone

pygame.init()


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (255,0,0)
blue = (255,0,0)
# a fourth parameter is degree of tranparency

font = pygame.font.SysFont(None,50)

display_height = 600 #size of screen
display_width = 700 #size of screen

FPS = 10 #frames per second

#surface that will be updated
gameDisplay = pygame.display.set_mode((display_width, display_height))  #tuple of scsreen size

pygame.display.set_caption('The Best Ice Cream Game Known to Man')

#pygame.display.update() #a parameter passes to this will update a specifici thing, but leaving it blank makes it update all
#pygame.display.flip() is the same thing as pygame.display.update



class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

BackGround = Background('space.png',[0,0])

def Cone():
	img = pygame.image.load('assets/img/cone.png')
	gameDisplay.blit(img, [200,400] )


def gameLoop():

	gameExit = False
	clock = pygame.time.Clock() #setting up frames per second
	#game loop
	while not gameExit:
		for event in pygame.event.get(): #getting the events
			if event.type == pygame.QUIT:  
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pass
					#put what we want to happen to objects here
				elif event.key == pygame.K_RIGHT:
					pass
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					pass


		#making the background
		#fill is something you apply to a surface object
		gameDisplay.fill(white)#one way to draw


		#between fill (above) and update is where you render other graphics
		gameDisplay.blit(BackGround.image, BackGround.rect)

		pygame.draw.rect(gameDisplay,white,[100, 100, 20,20])

		Cone()

		pygame.display.update() #updates the screen (for every run through the loop)

		clock.tick(FPS)#setting frames per second



gameLoop()
pygame.display.update()
time.sleep(2)
pygame.quit() #uninitalizes pygame
quit()#must have a quit 

