""" Abstract base class for graphical objects

    Note: Since it is an abstract base class (ABC), one cannot create objects
    of Graphic directly. Rather, one must create a new class that extends
    Graphic and implement all of the required methods.
"""
from abc import ABCMeta
import pygame


class Graphic(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta

    x_pos = None # int - the x-position of the graphic
    y_pos = None # int - the y-position of the graphic
    scale = None # int - a scalar used to adjust the size of the graphic
    velocity = None # (int,int) - the velocity of the object in m/s

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def move(self, delta_x, delta_y):
        """ Shifts the graphic

            delta_x: int - number of pixels to shift in the x-direction
            delta_y: int - number of pixels to shift in the y-direction
        """
        self.rect.move_ip(delta_x, delta_y)
