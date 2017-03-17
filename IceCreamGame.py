"""Ice Cream Game Code"""

from helpers import *
import time
import random

#imports graphic classes
from graphics.ice_cream_cone import *
from graphics.background import Background
from graphics.scoop import Scoop

#imports all obstacle making instances from making obstacles file
from making_obstacles import * 


class IceCreamGame:

    # ----- Constants -----
    
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    CONE_ACCELERATION = 4000  # pixels/second^2
    MAX_CONE_SPEED = 500  # pixels/second

    SCOOP_HEIGHT = 51  # height of ice cream scoop (px)
    WINDOW_HEIGHT = 600  # size of screen (px)
    WINDOW_WIDTH = 700  # size of screen (px)
    WINDOW_TITLE = 'The Best Ice Cream Game Known to Man'

    FPS = 30  # frames per second

    def __init__(self):
        pygame.init()  # initialize all imported pygame modules

        self.FONT = pygame.font.SysFont(None, 50)  # font for messages

        #surface that will be updated
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))  # input is tuple of screen size
        
        pygame.display.set_caption(self.WINDOW_TITLE)  # Caption for main screen
        pygame.key.set_repeat(30, 20)

        self.clock = pygame.time.Clock()  # set frame rate

        self.score = 0

    
        """Make Cone and Obstacles"""

        # parameters are scale, xpos, ypos NOTICE: SCALE does not work yet
        self.cone = IceCreamCone(10, 400, 600)

        #making obstacle instances. Calls the function 'making_obstacles' which returns a tuple of all the instances of each obstacle
        self.leaves = make_leaves(self.WINDOW_WIDTH)
        self.bees = make_bees(self.WINDOW_WIDTH)
        self.drones = make_drones(self.WINDOW_WIDTH)
        self.balloons = make_balloons(self.WINDOW_WIDTH)
        self.asteroids = make_asteroids(self.WINDOW_WIDTH)
        self.all_obstacles = []
        self.all_obstacles.extend(self.leaves)
        self.all_obstacles.extend(self.bees)
        self.all_obstacles.extend(self.drones)
        self.all_obstacles.extend(self.balloons)
        self.all_obstacles.extend(self.asteroids)
        self.scoops = make_scoops()

    def message_to_screen(self, msg, c, font, screen, x, y):
        """
        Making a message to user function

        :param msg: string you want to send as a message
        :param c: color of words for message
        :param font: pygame font to use
        :param screen: pygame screen to draw on
        :param x: x-coordinate you want to place message
        :param y: y-coordinate you want to place message
        """
        screen_text = font.render(msg, True, c)
        screen.blit(screen_text, [x, y])

    def check_for_scoop_collision(self):

        for scoop in self.scoops:
            scoop_cone_pos = self.cone.accelerate(0,0,1/self.FPS, self.MAX_CONE_SPEED) #location of cone's top scoop
            scoop_y_span = range(scoop.y_pos-100, scoop.y_pos+10) #y span of falling scoop
            scoop_x_span = range(scoop.x_pos-10, scoop.x_pos+110) #x span of falling scoop
            cone_x_span = range(scoop_cone_pos[0]-10, scoop_cone_pos[0]+100 ) #x span of cone location
            cone_y_span = range(scoop_cone_pos[1]-10, scoop_cone_pos[1]+100 )#y span of cone locaitons
            #sets X and Y to False initially
            x_collision = False
            y_collision = False
            #the following line checks that length of the list of elements are are in both the obs span and the scoop span
            #if the length is greater than 0, then there is a collision
            if len(list(set(scoop_x_span) & set(cone_x_span))) > 0: 
                x_collision = True
                
            #checks the scoops's y position for the range of the obstacle's y
            if len(list(set(scoop_y_span) & set(cone_y_span))) > 0: 
                y_collision = True
    
            randomplace = random.randint(0,self.WINDOW_WIDTH)
            #only exits the game if there is a collision in x and y
            if x_collision and y_collision:
                self.score += 1
                pygame.display.update()
                self.cone.add_scoop(Scoop(0, 0, 0.5, scoop.color))
                scoop.x_pos = randomplace
                scoop.y_pos = 0
                adj_height = self.SCOOP_HEIGHT
                self.cone.move(0, adj_height)
    
    def launch_game(self):
        """ Runs the game loop until the game ends

            :return 0 if the window should stay open until the user closes it, or -1 if the window should be closed immediately
        """
        while True:
            self.check_for_scoop_collision()

            for event in pygame.event.get():  # getting the events
                #running through events and effects of keyboard inputs
                if event.type == pygame.QUIT:
                    return -1  # Exit immediately
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.cone.accelerate(-self.CONE_ACCELERATION, 0, 1 / self.FPS, self.MAX_CONE_SPEED)
                    elif event.key == pygame.K_RIGHT:
                        self.cone.accelerate(self.CONE_ACCELERATION, 0, 1 / self.FPS, self.MAX_CONE_SPEED)
                    elif event.key == pygame.K_q:
                        return -1  # Exit immediately

            self.cone.update_state(1/self.FPS)

            # making the background
            change_in_y = 40 #reference for how fast the background changes
            scoops_before_change = 4 #reference for how many scoops the background stays the same before starting to move
            current_number_of_scoops = len(self.cone.scoops) #reference for number of scoops to gauge background

            #This background function is one gaint picture that goes form the ground to space.
            #The x component of the parameters and stays constant. The y compoent changes. At y = 0, it is the highest point in the picture
            #The lowest y value is 4400

            if current_number_of_scoops <= scoops_before_change: #if you have not reached x number of scoops, background stays the same
                background_y = -4400 #leaves background at bottom
            else: #if you get past the inital value of scoops
                new_y = (current_number_of_scoops-3)*change_in_y #correct ratio for changing background
                background_y = -4400 + new_y #changing background

            if background_y > 0:
                background_y = 0  #remember 0 is the top of the screen, so if it is 0, then you reached the end of the picture
                background_full = Background(os.path.join('assets', 'img', 'fullbackground.jpg'), [-11, background_y])
                self.screen.blit(background_full.image, background_full.rect)
                self.message_to_screen("You Win!", self.WHITE, self.FONT, self.screen, self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/2)
                pygame.display.update()
                time.sleep(2)
                return 0  # Wait for user to exit

            #full background image
            background_full = Background(os.path.join('assets', 'img', 'fullbackground.jpg'), [-11, background_y])
            self.screen.blit(background_full.image, background_full.rect)


            """Moving Obstacles at various locations in sky, each obstacle calls its own function"""


            self.leaves[0].display_moving_leaves(self.leaves, current_number_of_scoops, self.WINDOW_WIDTH, self.WINDOW_HEIGHT,self.screen)
            self.bees[0].display_moving_bees(self.bees, current_number_of_scoops, self.WINDOW_WIDTH, self.WINDOW_HEIGHT,self.screen)
            self.drones[0].display_moving_drones(self.drones, current_number_of_scoops, self.WINDOW_WIDTH, self.WINDOW_HEIGHT,self.screen)
            self.balloons[0].display_moving_ballons(self.balloons, current_number_of_scoops, self.WINDOW_WIDTH, self.WINDOW_HEIGHT,self.screen)
            self.asteroids[0].display_moving_asteroids(self.asteroids, current_number_of_scoops, self.WINDOW_WIDTH, self.WINDOW_HEIGHT,self.screen)

            self.scoops[0].display_moving_scoops(self.scoops, current_number_of_scoops, self.WINDOW_WIDTH, self.WINDOW_HEIGHT,self.screen)
            #list of obstacles for reference for collision handling


            #Collision Handling
            for obs in self.all_obstacles:  # Run through all obstacles
                #gives a tuple of the x and y location of the top  left corner of the sprite group
                scoop_cone_pos = self.cone.accelerate(0, 0, 0, self.MAX_CONE_SPEED)

                #sets range of x values for each obstacle.
                #obs = obstacle
                #each obstacle is about 100 pixels long
                obs_span = range(obs.x_pos, obs.x_pos+100)

                #sets top scoop's span, each is about 100 pixels long
                scoopx_span = range(scoop_cone_pos[0], scoop_cone_pos[0]+100 )

                #sets X and Y to False initially
                x_collision = False
                y_collision = False

                #the following line checks that length of the list of elements are are in both tqhe obs span and the scoop span
                #if the length is greater than 0, then there is a collision
                if len(list(set(obs_span) & set(scoopx_span))) > 0:
                    x_collision = True

                #checks the scoops's y position for the range of the obstacle's y
                if scoop_cone_pos[1] in range(obs.y_pos-10, obs.y_pos+ 10):
                    y_collision = True

                #only exits the game if there is a collision in x and y
                if x_collision and y_collision:
                    self.message_to_screen("You Lose!", self.RED, self.FONT, self.screen, self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/2)
                    pygame.display.update()
                    return 0  # Wait for user to exit

            "Drawing Cone"
            self.cone.draw(self.screen)

            # Display score
            self.message_to_screen('Score: %i' % self.score, self.BLUE, self.FONT, self.screen, 10, 10)

            pygame.display.update()  # updates the screen (for every run through the loop)

            self.clock.tick(self.FPS)  # setting frames per second


    def wait_for_close(self):
        """ Pause execution until the user clicks Close """
        time.sleep(2)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return


if __name__ == '__main__':
    game = IceCreamGame()
    exit_code = game.launch_game()
    if exit_code == 0:  # Player won or lost, wait to exit
        game.wait_for_close()
    pygame.quit()  # uninitializes pygame
    quit()  # must have a quit
