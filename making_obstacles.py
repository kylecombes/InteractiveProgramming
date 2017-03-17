
from graphics.obstacles.asteroid import Asteroid
from graphics.obstacles.leaf import Leaf
from graphics.obstacles.Drone import Drone
from graphics.obstacles.Balloon import Ballon
from graphics.obstacles.Bee import Bee
from graphics.scoop import Scoop
import random


def pick_random_place(display_width):
	return random.randint(0, display_width)


def make_leaves(display_width):
	"""Makes initial instances of leaf obstacles and returns the instances"""
	return [Leaf(pick_random_place(display_width), 0) for i in range(4)]


def make_asteroids(display_width):
	return [Asteroid(pick_random_place(display_width), 0) for i in range(6)]


def make_balloons(display_width):
	return [Ballon(pick_random_place(display_width), 0) for i in range(4)]


def make_drones(display_width):
	return [Drone(pick_random_place(display_width), 0) for i in range(4)]


def make_bees(display_width):
	return [Bee(pick_random_place(display_width), 0) for i in range(4)]


def make_scoops():
	return [Scoop(0, 0, 0.5) for i in range(7)]