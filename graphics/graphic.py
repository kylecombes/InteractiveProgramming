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

    def move(self, delta_x, delta_y):
        """ Shifts the graphic

            delta_x: int - number of pixels to shift in the x-direction
            delta_y: int - number of pixels to shift in the y-direction
        """
        move_ip(delta_x, delta_y)

    def get_bounds(self):
        """ Gets the bounds of the rectangle inscribing the object on the canvas.

            returns: a tuple in the form of (x1, y1, x2, y2)
        """
        r = self.rect
        return (r.x, r.y, r.x+r.w, r.y+r.h) if r else None
