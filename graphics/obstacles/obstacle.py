""" Abstract base class for obstacle objects

    Note: Since it is an abstract base class (ABC), one cannot create objects
    of Obstacle directly. Rather, one must create a new class that extends
    Obstacle and implement all of the required methods.
"""
from abc import ABCMeta, abstractmethod
from graphics.graphic import Graphic


class Obstacle(Graphic):
    __metaclass__ = ABCMeta


    def __init__(self):
        Graphic.__init__(self)
        self.x_velocity = 0
        self.y_velocity = 0

    @abstractmethod
    def draw(self, screen):
        """ Draws the scoop on the screen

            :param screen: a pygame Surface to draw on
         """
        raise NotImplementedError

    @abstractmethod
    def update_state(self, dt):
        """ Update the object position and any other state attributes

            :param dt: (int) the amount of time that has passed since the last call
         """
        raise NotImplementedError
