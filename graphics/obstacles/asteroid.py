from graphics.obstacles.obstacle import Obstacle
from helpers import *



class Asteroid(Obstacle):

    def __init__(self):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        Obstacle.__init__(self)
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'astroid.png'), -1)

    def draw(self, screen):
        """ Draws the Obstacles """
        screen.blit(self.image, (0,0))



    def move(self, key):
        """Move the obstacles with a certian speed"""
        xMove = 10
        yMove = 10
        self.rect.move_ip(xMove,yMove);

        #TODO ADD move to main loop

    def update_state(self, dt):
        # TODO Update the location of the asteroid
        pass
