"""Ice Cream Game Code"""

from helpers import *
import time
from graphics.ice_cream_cone import IceCreamCone
from graphics.background import Background
from graphics.scoop import Scoop
from graphics.obstacles.asteroid import Asteroid

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

#This backkground function is one gaint picture tha tgoes form the ground to space.
#The x compent of the parameters and stays constant. The y compent changes. At y = 0, it is the highest point in the picture
#The lowest y value is 4400

def message_to_screen(msg, color, xcord, ycord ):  #making a message to user
	screen_text = font.render(msg, True, color)
	screen.blit(screen_text, [xcord,ycord])


game_exit = False
clock = pygame.time.Clock()  # setting up frames per second
cone = IceCreamCone(10, 300, 300)
scoop_height = 51
obstacle1 = Asteroid()

# game loop
while not game_exit:
	for event in pygame.event.get():  # getting the events
		if event.type == pygame.QUIT:
			game_exit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				cone.move(-CONE_MOVE_INCREMENT, 0)
			elif event.key == pygame.K_RIGHT:
				cone.move(CONE_MOVE_INCREMENT, 0)
			#elif event.key == pygame.K_UP:
				#cone.move(0, -CONE_MOVE_INCREMENT)
			#elif event.key == pygame.K_DOWN:
				#cone.move(0, CONE_MOVE_INCREMENT)
			elif event.key == pygame.K_SPACE:
				cone.add_scoop(Scoop(0, 0, 0.5))
				if len(cone.scoops)>= scoops_before_change:
					cone.move(0, scoop_height) #makes the cone move down if the screen is moving up
			elif event.key == pygame.K_q:
				game_exit = True

	# making the background
	change_in_y = 20
	scoops_before_change = 5

	if len(cone.scoops)<= scoops_before_change:
		background_y = -4400
	else:
		new_y = (len(cone.scoops)-3)*change_in_y

		background_y = -4400 + new_y

	if background_y > 0:
		background_y = 0
		backgroundFull = Background(os.path.join('assets', 'img', 'fullbackground.jpg'), [-11, background_y])
		screen.blit(backgroundFull.image, backgroundFull.rect)
		message_to_screen("You Win!", white, display_width/2,display_height/2)
		pygame.display.update()
		time.sleep(2)
		game_exit = True
		quit()
		

		

	 

	backgroundFull = Background(os.path.join('assets', 'img', 'fullbackground.jpg'), [-11, background_y])
	screen.blit(backgroundFull.image, backgroundFull.rect)

	cone.draw(screen)
	#obstacle1.draw(screen)
	
	

	pygame.display.update()  # updates the screen (for every run through the loop)

	clock.tick(FPS)  # setting frames per second

#pygame.display.update()
# time.sleep(2)
pygame.quit()  # uninitializes pygame
quit()  # must have a quit
