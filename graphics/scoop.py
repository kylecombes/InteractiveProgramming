from graphics.graphic import Graphic
from helpers import *
import random


class Scoop(Graphic):

    def __init__(self, x_pos, y_pos, scale, color=None,):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        Graphic.__init__(self)

        choose_scoop = random.randint(0,3)
        types_of_cream = ['mint.png', 'scoop-white.png',  'pink.png', 'choc.png']
        self.color = color
        if self.color == 'scoop-white.png':
            self.color = 'scoop-white.png'
        if self.color == 'choc.png':
            self.color = 'choc.png'
        if self.color == 'mint.png':
            self.color = 'mint.png'
        if self.color == 'pink.png':
            self.color = 'pink.png'
        if self.color == None:
            self.color = types_of_cream[choose_scoop]
        self.image, self.rect = load_image(os.path.join('assets', 'img', self.color), -1)

        self.x_pos = x_pos
        self.y_pos = y_pos
        #self.rect.x = x_pos
        #self.rect.y = y_pos
        self.scale = scale

    def draw(self, screen):
        """ Draws the Obstacles """
        screen.blit(self.image, (self.x_pos,self.y_pos))  #The input tuble is the location in x and y respectivly 



    def display_moving_scoops(self, scoops, current_number_of_scoops, display_width, display_height, screen):
        """
        Displays moving leaves at intervals in the range of the correct background. Takes other
        instances of drone obstacle class to get several different obstacles.

        self2-self4: sequence of instances of obstacle
        current_number_of_scoops: num of scoops to gauge when to draw obstacles
        display_width: screen x size
        display_height: screen y size
        screen: screen to draw on
        """

        def move_format(obj):
            """
            just makes a format for moving the scoop obejcts 
            """
            obj.move_scoops(0,randomspeed,display_width, display_height)
            obj.draw(screen)
            if obj.y_pos > 600: 
                obj.y_pos = 0
                obj.x_pos = randomplace
                #obj.move_scoops(0,randomspeed,display_width, display_height)
                #obj.draw(screen)
            else:  
                pass


        randomspeed = random.randint(5,25)
        randomplace = random.randint(0,display_width)
        #the following statements checks for number of scoops to tell when to shoot obstacles
        #each move function takes an x direction speed (ususally 0) and a y direction seed
        # the display width and display height as also needed to move the obstacles
        if current_number_of_scoops >= 0:
            move_format(self)
        if current_number_of_scoops > 5:
            move_format(scoops[5])
        if current_number_of_scoops >10: 
            move_format(scoops[2])
        if current_number_of_scoops > 20:
            move_format(scoops[3])
        if current_number_of_scoops > 25:
            move_format(scoops[4])
        if current_number_of_scoops > 30:
            move_format(scoops[6])
        if current_number_of_scoops > 35:
            move_format(scoops[1])

        """
        KEY FOR NUMBER OF SCOOPS AND OBSTACLES:
        Number of Scoops: Obstacle in that range
        0-30: leaves
        30-50: bee
        50-80: drones
        80-110: ballons
        110-223: asteroids
        """

    def move_scoops(self, speed_x, speed_y, display_width, display_height):
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
        #if self.x_pos > display_width: 
        #    self.x_pos = display_width + 100
            #checks if obstacle is out of screen and stops it from moving
            #100 is how much over the edge of the screen it needs to be to stop moving
        #if self.y_pos > display_height:
        #    self.y_pos = display_height + 100
