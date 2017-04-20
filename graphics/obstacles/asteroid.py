from graphics.obstacles.obstacle import Obstacle
from helpers import *
import random
import math


class Asteroid(Obstacle):

    MAX_HORIZONTAL_SPEED = 30  # pixels/second
    MIN_HORIZONTAL_SPEED = 12  # pixels/second
    FALLING_SPEED = 30  # pixels/second


    def __init__(self, x_pos, y_pos):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        Obstacle.__init__(self, self.FALLING_SPEED, 0)
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'obstacles', 'asteroid.png'), -1)

        self.rect.x = x_pos
        self.rect.y = y_pos
        # Pick a random direction (left or right) and speed within the specified range
        direction = 1 if random.randint(0, 1) == 1 else -1
        self.x_velocity = random.randint(self.MIN_HORIZONTAL_SPEED, self.MAX_HORIZONTAL_SPEED) * direction


    def update_state(self, dt):
        """ Update the object position and any other state attributes

            :param dt: (int) the amount of time that has passed since the last call
         """
        dx = math.ceil(self.x_velocity * dt)
        # Also descend
        dy = math.ceil(self.y_velocity * dt)
        self.rect.move_ip(dx, dy)


