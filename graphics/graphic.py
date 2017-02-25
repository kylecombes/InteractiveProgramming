""" Abstract base class for graphical objects

    Note: Since it is an abstract base class (ABC), one cannot create objects
    of Graphic directly. Rather, one must create a new class that extends
    Graphic and implement all of the required methods.
"""
from abc import ABCMeta

class Graphic(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta

    x_pos = None # int - the x-position of the graphic
    y_pos = None # int - the y-position of the graphic
    scale = None # int - a scalar used to adjust the size of the graphic
    velocity = None # (int,int) - the velocity of the object in m/s

    def __init__(self):
        pass
    #
    # @abstractmethod
    # def draw(self, canvas):
    #     """ Draws the element on the given canvas. Called when updating the screen. """
    #     pass

    # @abstractmethod
    # def get_bounds(self):
    #     """ Gets the bounds of the rectangle inscribing the object on the canvas.
    #
    #         returns: a tuple in the form of (x1, y1, x2, y2)
    #     """
    #     pass
