from graphics.obstacles.obstacle import Obstacle
from helpers import *
import random


class Ballon(Obstacle):

    def __init__(self, x_pos, y_pos):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        Obstacle.__init__(self)
        self.image, self.rect = load_image(os.path.join('assets', 'img', 'purpleballon.png'), -1)

        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self, screen):
        """ Draws the Obstacles """
        screen.blit(self.image, (self.x_pos,self.y_pos))  #The input tuble is the location in x and y respectivly 

    def display_moving_ballons(self, self2, self3, self4, current_number_of_scoops, display_width, display_height, screen):
        """
        Displays moving leaves at intervals in the range of the correct background. Takes other
        instances of ballon obstacle class to get several differnt obstacles.
        self2-self4: sequence of instances of obstacle
        current_number_of_scoops: num of scoops to gauge when to draw obstacles
        display_width: screen x size
        display_height: screen y size
        screen: screen to draw on    
        """
        randomspeed = random.randint(5,15)
        #the following statements checks for number of scoops to tell when to shoot obstacles
        #each move function takes an x direction speed (ususally 0) and a y direction seed
        # the display width and display height as also needed to move the obstacles
        if current_number_of_scoops > 80:
            self.move_obstacle(0,randomspeed, display_width, display_height)
            self.draw(screen)
        if current_number_of_scoops > 87:
            self2.move_obstacle(-5,randomspeed,display_width, display_height)
            self2.draw(screen)
        if current_number_of_scoops >95:
            self3.move_obstacle(5,randomspeed,display_width, display_height)
            self3.draw(screen)
        if current_number_of_scoops > 100:
            self4.move_obstacle(0,randomspeed,display_width, display_height)
            self4.draw(screen)
        if current_number_of_scoops > 110:
            pass

        """
        KEY FOR NUMBER OF SCOOPS AND OBSTACLES:
        Number of Scoops: Obstacle in that range
        0-30: leaves
        30-50: bee
        50-80: drones
        80-110: ballons
        110-223: asteroids
        """

    def move_obstacle(self, speed_x, speed_y, display_width, display_height):
        """
        Take an object and a speed as a paramter and maves it move through the screen. 
        The speed is how many pixels it moves each loop though, 10 is a good number to start with.

        speed_x: speed in x position
        speed_y: speed in y position
        display_width: screen x size
        display_height: screen y size
        """
        self.x_pos += speed_x
        self.y_pos += speed_y
        if self.x_pos > display_width: 
            self.x_pos = display_width + 100
            #checks if obstacle is out of screen and stops it from moving
            #100 is how much over the edge of the screen it needs to be to stop moving
        if self.y_pos > display_height:
            self.y_pos = display_height + 100

