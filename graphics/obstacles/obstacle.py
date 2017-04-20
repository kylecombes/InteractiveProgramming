""" Abstract base class for obstacle objects

    Note: Since it is an abstract base class (ABC), one cannot create objects
    of Obstacle directly. Rather, one must create a new class that extends
    Obstacle and implement all of the required methods.
"""
from graphics.graphic import Graphic
import random
import math


class Obstacle(Graphic):


    def __init__(self, y_velocity, max_wind_speed):
        Graphic.__init__(self)
        self.x_velocity = 0
        self.y_velocity = y_velocity
        self.max_wind_speed = max_wind_speed

    def draw(self, screen):
        """ Draws the scoop on the screen

            :param screen: a pygame Surface to draw on
         """
        screen.blit(self.image, (self.rect.x,self.rect.y))  # The input tuple is the location in x and y respectively

    def update_state(self, dt):
        """ Update the object position and any other state attributes

            :param dt: (int) the amount of time that has passed since the last call
         """
        # Simulate wind blowing back and forth
        wind_effect = random.randrange(-self.max_wind_speed, self.max_wind_speed)
        self.x_velocity += wind_effect
        dx = math.ceil(self.x_velocity * dt)
        # Also descend
        dy = math.ceil(self.y_velocity * dt)
        self.rect.move_ip(dx, dy)
