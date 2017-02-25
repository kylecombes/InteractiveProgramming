# import Graphic
class IceCreamCone:

    def __init__(self,scale,x_pos,y_pos):
        """ Initializes an IceCreamCone object

            scale: an int used to scale the width and height to control the size
            x_pos: the starting x-position of the cone
            y_pos: the starting y-position of the cone
        """
        self.scale = scale

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add()
        self.scoops = list() # New list to keep track of scoops on cone

    def add_scoop(self, scoop):
        """ Adds a scoop to the top of the stack on the cone.

            Once a scoop has been handed off to the cone, the cone will handle
            redrawing it in the proper location. All other code should dispose
            of any references to the object to avoid accidental manipulations.
        """
        self.scoops.append(scoop)

    def draw(self, canvas):
        """ Draws the ice cream cone on the screen

            Implements required method from base class Graphic
        """
        self.sprite_group.draw(canvas)

class EmptyCone(Graphic):

    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('assets/img/cone.png',-1)
        if rect != None:
            self.rect = rect

    def draw(self, canvas):
        pass
