from graphics.graphic import Graphic
from helpers import *


class IceCreamCone(Graphic):

    SCOOP_CONE_OFFSET = 50  # draw the first scoop this many pixels below the top of the cone
    SCOOP_SCOOP_OFFSET = 50  # draw scoops this many pixels below the top of the previous scoop

    def __init__(self, scale, x_pos, y_pos):
        """ Initializes an IceCreamCone object

            scale: an int used to scale the width and height to control the size
            x_pos: the starting x-position of the cone
            y_pos: the starting y-position of the cone
        """
        Graphic.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        # Create a new sprite group to handle drawing all our sprites
        self.sprite_group = pygame.sprite.OrderedUpdates()
        # Create a new empty cone and add it to our sprite group
        self.cone = EmptyCone(x_pos,y_pos)
        self.sprite_group.add(self.cone)
        # Create a new list to keep track of the scoops on the cone
        self.scoops = list()
        #self.height = effective_scoop_height
        self.cone_img, self.rect = load_image(os.path.join('assets', 'img', 'cone.png'))
        # making the cone from the cone image

    def move(self, dx, dy, loc = False):
        """
        moves the sprite group of cone and scoops by dx and dy

        dx: change in x position
        dy: change in y position
        loc: if you want the location returned as a tuple or not
        """
        locations = [] # makes an empty list for storing locations
        for sprite in self.sprite_group.sprites(): # Move each sprite in our group
            sprite.rect.move_ip(dx, dy) #moves sprite
            locations.append((sprite.rect.x, sprite.rect.y)) #adds location to list
        if loc == True: #If you want the location returned, a set the last parameter to True
            return locations[-1] #returns a tuple of the x and y location of the top  left cornor of the sprite group
        

    def add_scoop(self, scoop):
        """ 
        Adds a scoop to the top of the stack on the cone.

        Once a scoop has been handed off to the cone, the cone will handle
        redrawing it in the proper location. All other code should dispose
        of any references to the object to avoid accidental manipulations.

        scoop: scoop sprite to be placed on top
        """
        # ----- Position the scoop correctly -----
        # Center the scoop over the cone
        scoop.rect.centerx = self.cone.rect.centerx
        # Put it on top and arranging it correctly
        scoop_count = len(self.scoops)
        effective_scoop_height = scoop.rect.height - self.SCOOP_SCOOP_OFFSET
        offset_from_cone_bottom = scoop_count*effective_scoop_height + self.cone.rect.height - self.SCOOP_CONE_OFFSET
        scoop.rect.bottom = self.cone.rect.bottom - offset_from_cone_bottom

        #adds to sprite group and appends to scoops object
        self.scoops.append(scoop)
        self.sprite_group.add(scoop)

    def draw(self, screen):
        """ 
        Draws the ice cream cone and stacked scoops on the screen 

        screen: screen object to be drawn on
        """
        self.sprite_group.draw(screen)




class EmptyCone(Graphic):

    def __init__(self, x_pos, y_pos, rect=None ):
        """ Initializes an EmptyCone object

            x_pos: the starting x-position of the cone
            y_pos: the starting y-position of the cone
        """
        Graphic.__init__(self)
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'cone.png'), -1)
        self.rect = self.image.get_rect()
        #sets x and y positions
        self.rect.right = x_pos 
        self.rect.bottom = y_pos
        if rect:
            self.rect = rect
