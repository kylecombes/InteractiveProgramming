"""Ice Cream Game Code"""

from helpers import *
import time
import random
from graphics.ice_cream_cone import IceCreamCone
from graphics.background import Background
from graphics.scoop import Scoop
from graphics.obstacles.asteroid import Asteroid
from graphics.obstacles.leaf import Leaf
from graphics.obstacles.Drone import Drone
from graphics.obstacles.Ballon import Ballon
from graphics.obstacles.Bee import Bee

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
obstacle1 = Asteroid(100,200)# start parameters are x_pos and y_pos
drone1 = Drone(100,100)
ballon1 = Ballon(200,300)


def pick_random_place():
	return random.randint(0,display_width)


#making leaf instances, if there a more concise way to do this????
leaf1 = Leaf(pick_random_place(), 0) 
leaf2 = Leaf(pick_random_place(), 0)
leaf3 = Leaf(pick_random_place(), 0)
leaf4 = Leaf(pick_random_place(), 0)

bee1 = Bee(pick_random_place(), 0) 
bee2 = Bee(pick_random_place(), 0)
bee3 = Bee(pick_random_place(), 0)
bee4 = Bee(pick_random_place(), 0)

drone1 = Drone(pick_random_place(), 0) 
drone2 = Drone(pick_random_place(), 0)
drone3 = Drone(pick_random_place(), 0)
drone4 = Drone(pick_random_place(), 0)

ballon1 = Ballon(pick_random_place(), 0) 
ballon2 = Ballon(pick_random_place(), 0)
ballon3 = Ballon(pick_random_place(), 0)
ballon4 = Ballon(pick_random_place(), 0)

asteroid1 = Asteroid(pick_random_place(), 0) 
asteroid2 = Asteroid(pick_random_place(), 0)
asteroid3 = Asteroid(pick_random_place(), 0)
asteroid4 = Asteroid(pick_random_place(), 0)
asteroid5 = Asteroid(pick_random_place(), 0)
asteroid6 = Asteroid(pick_random_place(), 0)

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


	"""
	KEY FOR NUMBER OF SCOOPS AND OBSTACLES:
	0-30: leaves
	30-50: bee
	50-80: drones
	80-110: ballons
	110-223: asteroids
	"""
	
	#Collision Handeling
	
	#coney = cone.scoop_height
	#coney = cone.height
	cone_x = sprite.rect.x
	#print(conex)
	#obstacle1.move_obstacle(10,5,display_width, display_height) #first two parameters are x speed and y speed
	#bee1.move_obstacle(10,0,display_width, display_height) #first two parameters are x speed and y speed
	#drone1.move_obstacle(5,0,display_width, display_height)
	#ballon1.move_obstacle(5,0,display_width, display_height)

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
