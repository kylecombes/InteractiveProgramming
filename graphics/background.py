""" The visual background for the game """
from helpers import *


class Background(pygame.sprite.Sprite):

	def __init__(self, image_file, location):
		"""
		Initializes an Background object

		image_file: image_file for background
		location: place to put on user screen
		"""
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image(image_file) #for our game, we have one giant backgroun picture
		#setting up position on user screen
		self.rect.left, self.rect.top = location
