from graphics.obstacles.obstacle import Obstacle
from helpers import *
import random


class Balloon(Obstacle):

    STARTING_MAX_HORIZONTAL_SPEED = 30  # pixels/second
    MAX_WIND_SPEED = 40  # pixels/second
    FALLING_SPEED = 10  # pixels/second

    def __init__(self, x_pos, y_pos):
        """ Initializes a new Scoop object at the given position and scale.

            :param x_pos: int - the x-coordinate of the top-left corner
            :param y_pos: int - the y-coordinate of the top-left corner
        """
        Obstacle.__init__(self, self.FALLING_SPEED, self.MAX_WIND_SPEED)
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'obstacles', 'balloon.png'), -1)
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.x_velocity = random.uniform(-1, 1)
        self.y_velocity = self.FALLING_SPEED
