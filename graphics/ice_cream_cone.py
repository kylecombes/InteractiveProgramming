from graphics.graphic import Graphic
from helpers import *
import math


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
        self.x_velocity = 0
        self.y_velocity = 0
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

    # def move(self, dx, dy, loc = False):
    #     """
    #     moves the sprite group of cone and scoops by dx and dy
    #
    #     dx: change in x position
    #     dy: change in y position
    #     loc: if you want the location returned as a tuple or not
    #     """

    def accelerate(self, ax, ay, dt, max_speed):
        """ Accelerate the cone and its contents in the corresponding direction

            :param ax: the acceleration component in the x-direction
            :param ay: the acceleration component in the y-direction
            :param dt: the amount of time for which to accelerate the cone
        """
        self.x_velocity += ax * dt
        if math.fabs(self.x_velocity) > max_speed:
            self.x_velocity = max_speed * (self.x_velocity / math.fabs(self.x_velocity))
        locations = [(s.rect.x, s.rect.y) for s in self.sprite_group.sprites()]
        return locations[-1]  # returns a tuple of the x and y location of the top  left cornor of the sprite group

    def update_state(self, dt):
        """ Update the state (position, etc.) of the cone given a period of elapsed time
        :param dt: the amount of time elapsed since the last update_state call
        """
        dx = math.ceil(self.x_velocity*dt)
        for sprite in self.sprite_group.sprites(): # Move each sprite in our group
            sprite.rect.move_ip(dx, 0)


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
        # Determine where the scoop should be placed such that it sits atop the stack
        scoop_count = len(self.scoops)
        effective_scoop_height = scoop.rect.height - self.SCOOP_SCOOP_OFFSET
        offset_from_cone_bottom = scoop_count*effective_scoop_height + self.cone.rect.height - self.SCOOP_CONE_OFFSET
        # Shift all the scoops and cone down
        for item in self.sprite_group.sprites():
            item.rect.move_ip(0, effective_scoop_height)
        # Put the scoop on top
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
