"""Ice Cream Game Code"""


import pygame
import time
# from helpers import *
from graphics.ice_cream_cone import IceCreamCone

pygame.init()


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
# a fourth parameter is degree of transparency

font = pygame.font.SysFont(None,50)

display_height = 600  # size of screen
display_width = 700  # size of screen

FPS = 10  # frames per second

#surface that will be updated
screen = pygame.display.set_mode((display_width, display_height))  # tuple of screen size

pygame.display.set_caption('The Best Ice Cream Game Known to Man')

#pygame.display.update() #a parameter passes to this will update a specified thing, but leaving it blank makes it update all
#pygame.display.flip() is the same thing as pygame.display.update

background = Background('space.png', [0,0])


gameLoop()
pygame.display.update()
time.sleep(2)
pygame.quit()  # uninitializes pygame
quit()  # must have a quit


class Background(pygame.sprite.Sprite):

	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location


def game_loop():

	game_exit = False
	clock = pygame.time.Clock()  # setting up frames per second
	cone = IceCreamCone(1, 100, 100)
	#game loop
	while not game_exit:
		for event in pygame.event.get():  # getting the events
			if event.type == pygame.QUIT:
				game_exit = True
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
		screen.fill(white)  # one way to draw


		#between fill (above) and update is where you render other graphics
		screen.blit(background.image, background.rect)

		pygame.draw.rect(screen, white, [100, 100, 20,20])

		cone.draw(screen)

		pygame.display.update()  # updates the screen (for every run through the loop)

		clock.tick(FPS)  # setting frames per second
