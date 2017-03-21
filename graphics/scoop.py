from graphics.graphic import Graphic
from helpers import *
import random


class Scoop(Graphic):

    SCOOP_LANDING_ZONE = 20  # The vertical distance from the bottom of the scoop to be used when determining
                             # if the scoop has landed on top of the cone

    def __init__(self, x_pos, y_pos, kind=None):
        """ Initializes a new Scoop object at the given position and scale.

            rect.x: int - the x-coordinate of the top-left corner
            rect.y: int - the y-coordinate of the top-left corner
        """
        Graphic.__init__(self)

        types_of_cream = ['mint.png', 'scoop-white.png',  'pink.png', 'choc.png']

        if kind is None:
            self.kind = random.choice(types_of_cream)
        else:
            self.kind = kind
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'scoops', self.kind), -1)

        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self, screen):
        """ Draws the Obstacles """
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, delta_x, delta_y):
        """ Move the scoop by the specified amounts

            :param delta_x: the number of pixels to move in the x-direction (right is positive)
            :param delta_y: the number of pixels to move in the y-direction (down in positive)
        """
        self.rect.move_ip(delta_x, delta_y)

    def get_bottom_rect(self):
        """ Returns a rect which represents the bottom of the scoop (to use
            when determining if a scoop has landed on the top of the cone
            or the top scoop).
        """
        return pygame.Rect(self.rect.left, self.rect.bottom - self.SCOOP_LANDING_ZONE, self.rect.width, self.SCOOP_LANDING_ZONE)
