""" The visual background for the game """
from helpers import *
import math

class Background(pygame.sprite.Sprite):

    def __init__(self, window_height, move_speed_scalar, move_speed_exponent):
        """ Initializes a Background object

            :param window_height: the height of the Surface the image is covering
        """
        pygame.sprite.Sprite.__init__(self)

        # Load the single giant background image
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'background.jpg'))

        # Position the bottom of the image at the bottom of the screen
        self.rect.bottom = window_height
        self.rect.left = 0

        self.window_height = window_height
        self.move_speed_scalar = move_speed_scalar
        self.move_speed_exponent = move_speed_exponent

    def shift_down(self, dy):
        """ Shifts the background image down

            :param dy: the number of pixels to shift the image down by
        """
        self.rect.bottom += dy

    def set_y(self, y_pos):
        """ Sets the y-position of the image relative to its starting position

            :param y_pos: the number of pixels the image should be shifted down from its starting location
        """
        self.rect.bottom = self.window_height + y_pos

    def update_state(self, elapsed_time):
        """ Updates the state (position, etc.) of the background

            :param elapsed_time: the amount of time (s) elapsed since the start of the game
        """
        self.rect.bottom = self.window_height + math.floor(self.move_speed_scalar * math.pow(elapsed_time, self.move_speed_exponent))

    def did_reach_end(self):
        """ Checks if the image has been scrolled all the way to the end

            :return True if image has been scrolled all the way, False otherwise
        """
        return self.rect.top >= 0

    def draw(self, screen):
        """ Draws the image on the screen

            :param screen: the Surface to draw on
        """
        screen.blit(self.image, self.rect)
