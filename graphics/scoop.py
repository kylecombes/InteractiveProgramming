from graphics.graphic import Graphic
from helpers import *
import random


class Scoop(Graphic):

    def __init__(self, x_pos, y_pos, scale):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        Graphic.__init__(self)

        choose_scoop = random.randint(0,3)
        types_of_cream = ['mint.png', 'scoop-white.png',  'pink.png', 'choc.png']
        self.image, self.rect = load_image(os.path.join('assets', 'img', types_of_cream[choose_scoop]), -1)

        self.rect.x = x_pos
        self.rect.y = y_pos
        self.scale = scale
