"""Ice Cream Game Code"""

from helpers import *
import time
import random

#imports graphic classes
from graphics.ice_cream_cone import IceCreamCone
from graphics.background import Background
from graphics.scoop import Scoop

#imports all obstacle making instances from making obstacles file
from making_obstacles import * 

pygame.init() #initalized all imported pygame modules
 
#making colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

CONE_MOVE_INCREMENT = 20  # pixels

font = pygame.font.SysFont(None, 50) #font for messages

display_height = 600  # size of screen
display_width = 700  # size of screen

FPS = 20  # frames per second

#surface that will be updated
screen = pygame.display.set_mode((display_width, display_height))  # input is tuple of screen size

pygame.display.set_caption('The Best Ice Cream Game Known to Man') # Caption for main screen
pygame.key.set_repeat(50, 20)

def message_to_screen(msg, color, xcord, ycord ):  
	"""
	Making a message to user function

	msg: string you want to send as a message
	color: color of words for message
	xcord: x cordinate you want to place message
	ycord: y cordinate you want to place message
	"""
	screen_text = font.render(msg, True, color)
	screen.blit(screen_text, [xcord,ycord])

game_exit = False #When this equals True, the game loop stops

clock = pygame.time.Clock()  # setting up frames per second
scoop_height = 51 #seeting scoop height for collision reference

"""Making Cone and Obstacles"""

# parameters are scale, xpos, ypos NOTICE: SCALE does not work yet
cone = IceCreamCone(10, 400, 600)

#making obstacle instances. Calls the function 'making_obstacles' which returns a tuple of all the instances of each obstacle 
leaf1, leaf2, leaf3, leaf4 = make_leaves(display_width)
bee1, bee2, bee3, bee4 = make_bees(display_width)
drone1, drone2, drone3, drone4 = make_drones(display_width)
ballon1, ballon2, ballon3, ballon4 = make_ballons(display_width)
asteroid1, asteroid2, asteroid3, asteroid4, asteroid5, asteroid6 = make_asteroids(display_width)

# game loop
while not game_exit:
	for event in pygame.event.get():  # getting the events
		#running through events and effects of keyboard inputs
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
	change_in_y = 20 #reference for how fast the background changes
	scoops_before_change = 5 #reference for how many scoops the background stays the same before starting to move
	current_number_of_scoops = len(cone.scoops) #reference for number of scoops to gauge background

	#This background function is one gaint picture that goes form the ground to space.
	#The x compoent of the parameters and stays constant. The y compoent changes. At y = 0, it is the highest point in the picture
	#The lowest y value is 4400

	if current_number_of_scoops <= scoops_before_change: #if you have not reached x number of scoops, background stays the same
		background_y = -4400 #leaves background at bottom
	else: #if you get past the inital value of scoops
		new_y = (current_number_of_scoops-3)*change_in_y #correct ratio for changing background
		background_y = -4400 + new_y #changing background

	if background_y > 0:
		background_y = 0  #remember 0 is the top of the screen, so if it is 0, then you reached the end of the picture
		backgroundFull = Background(os.path.join('assets', 'img', 'fullbackground.jpg'), [-11, background_y])
		screen.blit(backgroundFull.image, backgroundFull.rect) 
		message_to_screen("You Win!", white, display_width/2,display_height/2) #giving message
		pygame.display.update()
		time.sleep(2)
		game_exit = True #stops game loop
		quit() #exits game screen

	#full background image
	backgroundFull = Background(os.path.join('assets', 'img', 'fullbackground.jpg'), [-11, background_y])
	screen.blit(backgroundFull.image, backgroundFull.rect)


	"""Moveing Obstacles at various locations in sky, each obstacle calls its own function"""


	leaf1.display_moving_leaves(leaf2, leaf3, leaf4, current_number_of_scoops, display_width, display_height, screen)
	bee1.display_moving_bees(bee2, bee3, bee4, current_number_of_scoops, display_width, display_height, screen)
	drone1.display_moving_drones(drone2, drone3, drone4, current_number_of_scoops, display_width, display_height, screen)
	ballon1.display_moving_ballons(ballon2, ballon3, ballon4, current_number_of_scoops, display_width, display_height, screen)
	asteroid1.display_moving_asteroids(asteroid2, asteroid3, asteroid4, asteroid5, asteroid6, current_number_of_scoops, display_width, display_height, screen)

	#list of obstacles for reference for collision handeling 
	list_of_obstacles = [leaf1, leaf2, leaf3, leaf4, bee1, bee2, bee3, bee4, drone1, drone2, drone3, drone4, ballon1, ballon2, ballon3, ballon4, asteroid1, asteroid2, asteroid3, asteroid4, asteroid5, asteroid6]
	
	#Collision Handeling
	for obs in list_of_obstacles: #running through all obstacles
		#gives a tuple of the x and y location of the top  left cornor of the sprite group
		scoop_cone_pos = cone.move(0,0,True) 

		#sets range of x values for each obstacle.
		#obs = obstacle
		#each obstacle is about 100 pixels long
		obs_span = range(obs.x_pos, obs.x_pos+100) 

		#sets top scoop's span, each is about 100 pixels long
		scoopx_span = range(scoop_cone_pos[0], scoop_cone_pos[0]+100 )

		#sets X and Y to False initally
		X_collision = False
		Y_collision = False

		#the following line checks that length of the list of elements are are in both the obs span and the scoop span
		#if the length is greater than 0, then there is a collision
		if len(list(set(obs_span) & set(scoopx_span))) > 0: 
			X_collision = True

		#checks the scoops's y position for the range of the obstacle's y
		if scoop_cone_pos[1] in range(obs.y_pos-10, obs.y_pos+ 10):
			Y_collision = True

		#only exits the game if there is a collision in x and y
		if X_collision and Y_collision:
			message_to_screen("You Lose!", red, display_width/2,display_height/2) #send you lose message to user
			pygame.display.update() 
			time.sleep(2)
			game_exit = True
			quit()

	"Drawing Cone"
	cone.draw(screen)

	pygame.display.update()  # updates the screen (for every run through the loop)

	clock.tick(FPS)  # setting frames per second

pygame.quit()  # uninitializes pygame
quit()  # must have a quit
