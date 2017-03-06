
from graphics.obstacles.asteroid import Asteroid
from graphics.obstacles.leaf import Leaf
from graphics.obstacles.Drone import Drone
from graphics.obstacles.Ballon import Ballon
from graphics.obstacles.Bee import Bee
import random

def pick_random_place(display_width):
	return random.randint(0,display_width)

def make_leaves(display_width):
	"""Makes inital instances of leaf obstacles and returns the instances"""
	leaf1 = Leaf(pick_random_place(display_width), 0) 
	leaf2 = Leaf(pick_random_place(display_width), 0)
	leaf3 = Leaf(pick_random_place(display_width), 0)
	leaf4 = Leaf(pick_random_place(display_width), 0)
	return leaf1, leaf2, leaf3, leaf4

def make_asteroids(display_width):
	asteroid1 = Asteroid(pick_random_place(display_width), 0) 
	asteroid2 = Asteroid(pick_random_place(display_width), 0)
	asteroid3 = Asteroid(pick_random_place(display_width), 0)
	asteroid4 = Asteroid(pick_random_place(display_width), 0)
	asteroid5 = Asteroid(pick_random_place(display_width), 0)
	asteroid6 = Asteroid(pick_random_place(display_width), 0)
	return asteroid1, asteroid2, asteroid3, asteroid4, asteroid5, asteroid6
	
def make_ballons(display_width):
	ballon1 = Ballon(pick_random_place(display_width), 0) 
	ballon2 = Ballon(pick_random_place(display_width), 0)
	ballon3 = Ballon(pick_random_place(display_width), 0)
	ballon4 = Ballon(pick_random_place(display_width), 0)
	return ballon1, ballon2, ballon3, ballon4

def make_drones(display_width):
	drone1 = Drone(pick_random_place(display_width), 0) 
	drone2 = Drone(pick_random_place(display_width), 0)
	drone3 = Drone(pick_random_place(display_width), 0)
	drone4 = Drone(pick_random_place(display_width), 0)
	return drone1, drone2, drone3, drone4

def make_bees(display_width):
	bee1 = Bee(pick_random_place(display_width), 0) 
	bee2 = Bee(pick_random_place(display_width), 0)
	bee3 = Bee(pick_random_place(display_width), 0)
	bee4 = Bee(pick_random_place(display_width), 0)
	return bee1, bee2, bee3, bee4