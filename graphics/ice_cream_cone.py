from graphics.graphic import Graphic
from helpers import *
import math


class IceCreamCone(Graphic):

    SCOOP_CONE_OFFSET = 50  # draw the first scoop this many pixels below the top of the cone
    SCOOP_SCOOP_OFFSET = 50  # draw scoops this many pixels below the top of the previous scoop

    SCOOP_LANDING_ZONE = 20  # consider a scoop to have landed on top of the cone or another scoop if it is within
                             # this many pixels of the top of the cone or top scoop (if any)

    def __init__(self, x_pos, y_pos):
        """ Initializes an IceCreamCone object

            scale: an int used to scale the width and height to control the size
            x_pos: the starting x-position of the cone
            y_pos: the starting y-position of the cone
        """
        Graphic.__init__(self)
        # Initialize our velocities to zero
        self.x_velocity = 0
        self.y_velocity = 0
        # Create a new sprite group to handle drawing all our sprites
        self.sprite_group = pygame.sprite.OrderedUpdates()
        # Create a new empty cone and add it to our sprite group
        self.cone = EmptyCone(x_pos, y_pos)
        self.sprite_group.add(self.cone)
        # Create a new list to keep track of the scoops on the cone
        self.scoops = list()

    def accelerate(self, ax, ay, dt, max_speed, due_to_drag=False):
        """ Accelerate the cone and its contents in the corresponding direction

            :param ax: the acceleration component in the x-direction
            :param ay: the acceleration component in the y-direction
            :param dt: the amount of time for which to accelerate the cone
            :param max_speed: the maximum speed at which the cone can travel
            :param due_to_drag: whether or not this acceleration is due to drag, in
                   which case the velocity should not switch signs, but rather go to zero
        """
        dv = ax * dt
        # Check if we're decelerating due to drag and reaching 0
        if due_to_drag and math.fabs(self.x_velocity) < math.fabs(dv):
            self.x_velocity = 0
        else:
            self.x_velocity += dv
        # Check if we're now going faster than our max allowed speed
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
        effective_scoop_height = scoop.rect.height - self.SCOOP_SCOOP_OFFSET
        scoop_count = len(self.scoops)
        if scoop_count > 0:
            current_top = self.scoops[-1].rect.top
            offset_from_cone_bottom = self.cone.rect.bottom - current_top - self.SCOOP_SCOOP_OFFSET
        else:
            current_top = self.cone.rect.top
            offset_from_cone_bottom = self.cone.rect.bottom - current_top - self.SCOOP_CONE_OFFSET

        if len(self.scoops) > 2:
            # Shift all the scoops and cone down
            for item in self.sprite_group.sprites():
                item.rect.move_ip(0, effective_scoop_height)
        # Put the scoop on top
        scoop.rect.bottom = self.cone.rect.bottom - offset_from_cone_bottom

        #adds to sprite group and appends to scoops object
        self.scoops.append(scoop)
        self.sprite_group.add(scoop)

    def get_top_scoop(self):
        """" Returns the scoop at the top of the stack, None if empty """
        return self.scoops[-1] if len(self.scoops) > 0 else None

    def get_rect(self):
        """" Returns the rect enclosing the entire cone and scoop stack """
        r = self.cone.rect.copy()
        for scoop in self.scoops:
            r.union_ip(scoop.rect)
        return r

    def get_cone_top_rect(self):
        """" Returns a rect which represents the top of the cone (to use
             when determining if a scoop has landed on the top of the cone
             or the top scoop).
         """
        # Get the rect of whatever object is at the top of our stack (top scoop if any, cone otherwise)
        r_model = self.scoops[-1].rect if len(self.scoops) > 0 else self.cone.rect
        # Return a new rect of the proper height and aligned with the top of the old rect
        return pygame.Rect(r_model.left, r_model.top, r_model.width, self.SCOOP_LANDING_ZONE)

    def draw(self, screen):
        """ 
        Draws the ice cream cone and stacked scoops on the screen 

        screen: screen object to be drawn on
        """
        self.sprite_group.draw(screen)




class EmptyCone(Graphic):

    def __init__(self, x_pos, y_pos):
        """ Initializes an EmptyCone object

            x_pos: the starting x-position of the cone
            y_pos: the starting y-position of the cone
        """
        Graphic.__init__(self)
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'cone.png'), -1)
        self.rect.x = x_pos
        self.rect.y = y_pos
