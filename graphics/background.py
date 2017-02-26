""" The visual background for the game """
from helpers import *


class Background(pygame.sprite.Sprite):

	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image(image_file)
		self.rect.left, self.rect.top = location
