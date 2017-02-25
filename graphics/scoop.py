import Graphic
class Scoop(Graphic):

    def __init__(self,x_pos,y_pos,scale):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        self.image, self.rect = load_image('assets/img/scoop-white.png',-1)
