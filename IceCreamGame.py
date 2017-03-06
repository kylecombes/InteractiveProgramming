"""Ice Cream Game Code"""

from helpers import *
import time
import random
from graphics.ice_cream_cone import IceCreamCone
from graphics.background import Background
from graphics.scoop import Scoop
from making_obstacles import *

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

scoop_height = 51



"""Making Cone and Obstacles"""

cone = IceCreamCone(10, 400, 600) # parameters are scale, xpos, ypos NOTICE: SCALE does not work yet


def pick_random_place(display_width):
	return random.randint(0,display_width)


#making obstacle instances. Calls the function 'making_obstacles' which returns a tuple of all the instances of each obstacle 

leaf1, leaf2, leaf3, leaf4 = make_leaves(display_width)
bee1, bee2, bee3, bee4 = make_bees(display_width)
drone1, drone2, drone3, drone4 = make_drones(display_width)
ballon1, ballon2, ballon3, ballon4 = make_ballons(display_width)
asteroid1, asteroid2, asteroid3, asteroid4, asteroid5, asteroid6 = make_asteroids(display_width)

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
			elif event.key == pygame.K_SPACE:
				cone.add_scoop(Scoop(0, 0, 0.5))
				if len(cone.scoops)>= scoops_before_change:
					cone.move(0, scoop_height) #makes the cone move down if the screen is moving up
			elif event.key == pygame.K_q:
				game_exit = True

	# making the background
	change_in_y = 20
	scoops_before_change = 5
	current_number_of_scoops = len(cone.scoops)

	if current_number_of_scoops<= scoops_before_change:
		background_y = -4400
	else:
		new_y = (current_number_of_scoops-3)*change_in_y

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


	"""Moveing Obstacles at various locations in sky"""


	leaf1.display_moving_leaves(leaf2, leaf3, leaf4, current_number_of_scoops, display_width, display_height, screen)
	bee1.display_moving_bees(bee2, bee3, bee4, current_number_of_scoops, display_width, display_height, screen)
	drone1.display_moving_drones(drone2, drone3, drone4, current_number_of_scoops, display_width, display_height, screen)
	ballon1.display_moving_ballons(ballon2, ballon3, ballon4, current_number_of_scoops, display_width, display_height, screen)
	asteroid1.display_moving_asteroids(asteroid2, asteroid3, asteroid4, asteroid5, asteroid6, current_number_of_scoops, display_width, display_height, screen)

	list_of_opstacles= [leaf1, leaf2, leaf3, leaf4, bee1, bee2, bee3, bee4, drone1, drone2, drone3, drone4, ballon1, ballon2, ballon3, ballon4, asteroid1, asteroid2, asteroid3, asteroid4, asteroid5, asteroid6]

	"""
	KEY FOR NUMBER OF SCOOPS AND OBSTACLES:
	0-30: leaves
	30-50: bee
	50-80: drones
	80-110: ballons
	110-223: asteroids
	"""
	
	#Collision Handeling
	for obs in list_of_opstacles:
		scoop_cone_pos = cone.move(0,0,True) #gives a tuple of the x and y location of the top  left cornor of the sprite group
		ops_span = range(obs.x_pos, obs.x_pos+100)
		scoopx_span = range(scoop_cone_pos[0]-10, scoop_cone_pos[0]+100 + 10)
		X_collision = False
		Y_collision = False
		if len(list(set(ops_span) & set(scoopx_span))) > 0:
			X_collision = True
		if scoop_cone_pos[1] in range(obs.y_pos-10, obs.y_pos+ 10):
			Y_collision = True
		if X_collision and Y_collision:
			message_to_screen("You Lose!", red, display_width/2,display_height/2)
			pygame.display.update() 
			time.sleep(2)
			game_exit = True
			quit()



	#bee1.draw(screen)
	cone.draw(screen)
	#obstacle1.draw(screen)
	
	#drone1.draw(screen)
	#ballon1.draw(screen)

	pygame.display.update()  # updates the screen (for every run through the loop)

	clock.tick(FPS)  # setting frames per second

#pygame.display.update()
# time.sleep(2)
pygame.quit()  # uninitializes pygame
quit()  # must have a quit
