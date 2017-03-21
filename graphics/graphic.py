""" Abstract base class for graphical objects

    Note: Since it is an abstract base class (ABC), one cannot create objects
    of Graphic directly. Rather, one must create a new class that extends
    Graphic and implement all of the required methods.
"""
from abc import ABCMeta
import pygame


class Graphic(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta

    x_pos = None  # int - the x-position of the graphic
    y_pos = None  # int - the y-position of the graphic
    scale = None  # int - a scalar used to adjust the size of the graphic
    velocity = None  # (int,int) - the velocity of the object in m/s

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def move(self, delta_x, delta_y):
        """ Shifts the graphic

            delta_x: int - number of pixels to shift in the x-direction
            delta_y: int - number of pixels to shift in the y-direction
        """
        if hasattr(self, 'rect'):
            self.rect.move_ip(delta_x, delta_y)
        else:
            raise Exception("Attribute 'rect' not defined for %s" % self.__class__)

    def is_on_screen(self, screen_width, screen_height, margin=0):
        """ Checks to see if the item is on or off the screen

            :param screen_width: the width of the Surface the object being is drawn on
            :param screen_height: the height of the Surface the object being is drawn on
            :param margin: an optional shift of the screen edges. Positive shifts the screen edges in, negative shifts out.
            :returns True if the object is at least partially within the bounds of the screen (w/margin), False if it is entirely outside.
        """
        if hasattr(self, 'rect'):
            return not (self.rect.right < margin
                        or self.rect.left > screen_width - margin
                        or self.rect.bottom < margin
                        or self.rect.top > screen_height - margin)
        else:
            raise Exception("Attribute 'rect' not defined for %s" % self.__class__)
