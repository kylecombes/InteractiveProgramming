"""Ice Cream Game Code"""

from helpers import *
from graphics.ice_cream_cone import IceCreamCone
from graphics.background import Background
from graphics.scoop import Scoop

pygame.init()


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
CONE_MOVE_INCREMENT = 10  # pixels

# a fourth parameter is degree of transparency

font = pygame.font.SysFont(None, 50)

display_height = 600  # size of screen
display_width = 700  # size of screen

FPS = 20  # frames per second

#surface that will be updated
screen = pygame.display.set_mode((display_width, display_height))  # tuple of screen size

pygame.display.set_caption('The Best Ice Cream Game Known to Man')
pygame.key.set_repeat(50, 20)

#pygame.display.update() #a parameter passes to this will update a specified thing, but leaving it blank makes it update all
#pygame.display.flip() is the same thing as pygame.display.update

background = Background(os.path.join('assets', 'img', 'space_bg.png'), [0, 0])

game_exit = False
clock = pygame.time.Clock()  # setting up frames per second
cone = IceCreamCone(1, 100, 100)
# game loop
while not game_exit:
	for event in pygame.event.get():  # getting the events
		if event.type == pygame.QUIT:
			game_exit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				cone.move(-CONE_MOVE_INCREMENT, 0)
			# put what we want to happen to objects here
			elif event.key == pygame.K_RIGHT:
				cone.move(CONE_MOVE_INCREMENT, 0)
			elif event.key == pygame.K_UP:
				cone.move(0, -CONE_MOVE_INCREMENT)
			elif event.key == pygame.K_DOWN:
				cone.move(0, CONE_MOVE_INCREMENT)
			elif event.key == pygame.K_SPACE:
				cone.add_scoop(Scoop(0, 0, 1))
			elif event.key == pygame.K_q:
				game_exit = True

	# making the background
	screen.blit(background.image, background.rect)

	cone.draw(screen)

	pygame.display.update()  # updates the screen (for every run through the loop)

	clock.tick(FPS)  # setting frames per second

pygame.display.update()
# time.sleep(2)
pygame.quit()  # uninitializes pygame
quit()  # must have a quit
