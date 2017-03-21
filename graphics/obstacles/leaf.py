from graphics.obstacles.obstacle import Obstacle
from helpers import *
import random
import math


class Leaf(Obstacle):

    STARTING_MAX_HORIZONTAL_SPEED = 30  # pixels/second
    MAX_WIND_SPEED = 30  # pixels/second
    FALLING_SPEED = 10  # pixels/second

    def __init__(self, x_pos, y_pos):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        Obstacle.__init__(self)
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'obstacles', 'leaf.png'), -1)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.y_velocity = self.FALLING_SPEED

    def draw(self, screen):
        """ Draws the Obstacles """
        screen.blit(self.image, (self.rect.x,self.rect.y))  # The input tuple is the location in x and y respectively

    def update_state(self, dt):
        """ Update the object position and any other state attributes

            :param dt: (int) the amount of time that has passed since the last call
         """
        # Simulate wind blowing back and forth
        wind_effect = random.randrange(-self.MAX_WIND_SPEED, self.MAX_WIND_SPEED)
        self.x_velocity += wind_effect
        dx = math.ceil(self.x_velocity * dt)
        # Also descend
        dy = math.ceil(self.y_velocity * dt)
        self.rect.move_ip(dx, dy)
