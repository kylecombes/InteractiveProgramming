from graphics.obstacles.obstacle import Obstacle
from helpers import *



class Drone(Obstacle):

    def __init__(self, x_pos, y_pos):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        Obstacle.__init__(self)
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'drone.png'), -1)

        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self, screen):
        """ Draws the Obstacles """
        screen.blit(self.image, (self.x_pos,self.y_pos))  #The input tuble is the location in x and y respectivly 



    def move_obstacle(self, speed_x, speed_y, display_width, display_height):
        """
        Take an object and a speed as a paramter and maves it move through the screen. 

        The speed is how many pixels it moves each loop though, 10 is a good number to start with.

        """
        self.x_pos += speed_x
        self.y_pos += speed_y
        if self.x_pos > display_width: 
            self.x_pos = display_width + 100
        if self.y_pos > display_height:
            self.y_pos = display_height + 100

        #TODO ADD move to main loop

    def update_state(self, dt):
        # TODO Update the location of the asteroid
        pass
