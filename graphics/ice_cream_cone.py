
import Graphic
import os, syss
import pygame
from pygame.locals import *
from helpers import *

class IceCreamCone():

    def __init__(self, scale, x_pos, y_pos):
        """ Initializes an IceCreamCone object

            scale: an int used to scale the width and height to control the size
            x_pos: the starting x-position of the cone
            y_pos: the starting y-position of the cone
        """
        # Create a new sprite group to handle drawing all our sprites
        self.sprite_group = pygame.sprite.Group()
        # Create a new empty cone and add it to our sprite group
        self.cone = EmptyCone()
        self.sprite_group.add(cone)
        # Create a new list to keep track of the scoops on the cone
        self.scoops = list()
        self.con_img = pygame.image.load('assets/img/cone.png')

    def move(self, dx, dy):
        # Move each sprite in our group
        for sprite in self.sprite_group.sprites:
            sprite.rect.move_ip(xMove,yMove)

    def add_scoop(self, scoop):
        """ Adds a scoop to the top of the stack on the cone.

            Once a scoop has been handed off to the cone, the cone will handle
            redrawing it in the proper location. All other code should dispose
            of any references to the object to avoid accidental manipulations.
        """
        self.scoops.append(scoop)
        self.sprite_group.add(scoop)

    def draw(self, screen):
        """ Draws the ice cream cone and stacked scoops on the screen """
        # Draw the cone
        gameDisplay.blit(self.cone_img, self.rect)
        # Draw the scoops
        self.sprite_group.draw(screen)

class EmptyCone():

    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('assets/img/cone.png',-1)
        self.rect = self.image.get_rect()
        if rect != None:
            self.rect = rect
