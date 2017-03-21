"""Ice Cream Game Code"""

import time
from graphics.ice_cream_cone import *
from graphics.background import Background
import random
from graphics.scoop import Scoop
from graphics.obstacles.asteroid import Asteroid
from graphics.obstacles.balloon import Balloon
from graphics.obstacles.bee import Bee
from graphics.obstacles.drone import Drone
from graphics.obstacles.leaf import Leaf


class IceCreamGame:

    # ----- Constants -----

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    OBSTACLE_TYPES = [Leaf.__class__, Bee.__class__, Balloon.__class__, Drone.__class__, Asteroid.__class__]

    CONE_ACCELERATION = 80  # pixels/second^2
    CONE_DRAG_ACCELERATION = 40  # pixels/second^2
    MAX_CONE_SPEED = 500  # pixels/second

    SCOOP_HEIGHT = 51  # height of ice cream scoop (px)
    WINDOW_HEIGHT = 600  # size of screen (px)
    WINDOW_WIDTH = 700  # size of screen (px)
    WINDOW_TITLE = 'The Best Ice Cream Game Known to Man'

    FPS = 20  # refresh rate (frames per second)

    BG_CHANGE_SPEED_SCALAR = FPS / 30
    BG_CHANGE_SPEED_EXP = 1.5

    def __init__(self):
        pygame.init()  # initialize all imported pygame modules

        self.FONT = pygame.font.SysFont(None, 50)  # font for messages

        # Initialize drawing canvas and background
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.background = Background(self.WINDOW_HEIGHT, self.BG_CHANGE_SPEED_SCALAR, self.BG_CHANGE_SPEED_EXP)

        # Set window title
        pygame.display.set_caption(self.WINDOW_TITLE)

        # Set key repeat delay and interval
        pygame.key.set_repeat(30, 20)

        # Initialize clock for timing refreshes
        self.clock = pygame.time.Clock()

        # Initialize counters to keep track of time (s) till next scoop and obstacle should be released
        # (could be done with separate timers, but don't need to be that precise)
        self.time_till_next_obstacle_release = 5
        self.time_till_next_scoop_release = 0.5

        self.cone = IceCreamCone(400, self.WINDOW_HEIGHT - 230)
        self.all_obstacles = list()
        self.falling_scoops = list()

        # Initialize player's score
        self.score = 0


    def message_to_screen(self, msg, c, x, y):
        """
        Making a message to user function

        :param msg: string you want to send as a message
        :param c: color of words for message
        :param x: x-coordinate you want to place message
        :param y: y-coordinate you want to place message
        """
        screen_text = self.FONT.render(msg, True, c)
        self.screen.blit(screen_text, [x, y])

    def check_for_scoop_collision(self):

        # Get the object on the top of the cone stack (normally a scoop,
        # unless there are no scoops, in which case it's the cone)
        top_of_cone_stack = self.cone.get_top_scoop()
        if top_of_cone_stack is None:
            top_of_cone_stack = self.cone.cone

        # Check all falling scoops for collision with top item
        for scoop in self.falling_scoops:
            if pygame.sprite.collide_rect(scoop, top_of_cone_stack):  # Caught falling scoop
                self.score += 1
                self.falling_scoops.remove(scoop)
                self.cone.add_scoop(scoop)

    def launch_game(self):
        """ Runs the game loop until the game ends

            :return 0 if the window should stay open until the user closes it, or -1 if the window should be closed immediately
        """
        while True:

            # Keep track of whether or not the user accelerated the cone with the keyboard
            cone_did_accelerate = False

            # First, respond to any user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1  # Exit immediately
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.cone.accelerate(-self.CONE_ACCELERATION, 0, 1 / self.FPS, self.MAX_CONE_SPEED)
                        cone_did_accelerate = True
                    elif event.key == pygame.K_RIGHT:
                        self.cone.accelerate(self.CONE_ACCELERATION, 0, 1 / self.FPS, self.MAX_CONE_SPEED)
                        cone_did_accelerate = True
                    elif event.key == pygame.K_q:
                        return -1  # Exit immediately


            # If user didn't accelerate cone, simulate drag slowing it down
            if not cone_did_accelerate and self.cone.x_velocity != 0:
                current_vel_sign = self.cone.x_velocity / math.fabs(self.cone.x_velocity)
                self.cone.accelerate(-current_vel_sign*self.CONE_DRAG_ACCELERATION, 0, 1 / self.FPS, self.MAX_CONE_SPEED, True)

            """ Update positions of objects """
            for i, scoop in enumerate(self.falling_scoops):
                scoop.move(0, 1)  # TODO Remove hardcoding
                # Remove off-screen scoops
                if scoop.rect.top > self.WINDOW_HEIGHT:
                    self.falling_scoops.remove(scoop)
            for obstacle in self.all_obstacles:
                obstacle.update()
                # Remove off-screen obstacles
                if obstacle.rect.top > self.WINDOW_HEIGHT:
                    self.all_obstacles.remove(obstacle)


            """ ---- Collision Detection ---- """
            # Scoops onto cone (or top scoop on stack)
            target_rect = self.cone.get_cone_top_rect()
            for scoop in self.falling_scoops:
                falling_rect = scoop.get_bottom_rect()
                if target_rect.colliderect(falling_rect):
                    # Scoop collided with top of ice cream cone stack, so add it to cone stack
                    self.cone.add_scoop(scoop)
                    self.falling_scoops.remove(scoop)
                    self.score += 1
            # Obstacles with cone or scoop stack
            cone_rect = self.cone.get_rect()
            for obstacle in self.all_obstacles:
                if cone_rect.colliderect(obstacle.rect):
                    # Collision! Display message and exit loop
                    self.message_to_screen("You Lose!", self.RED, self.WINDOW_WIDTH / 3, self.WINDOW_HEIGHT / 3)
                    pygame.display.update()
                    return 0  # Wait for user to exit

            elapsed_time = pygame.time.get_ticks() / 1000  # The number of seconds elapsed since the start of the game


            """ ---- Falling Object Generation ---- """
            # -- Obstacle Generation -- #
            # Decrement obstacle release timer
            if self.time_till_next_obstacle_release > 0:
                self.time_till_next_obstacle_release -= 1 / self.FPS
            # Check if timer has reached zero
            if self.time_till_next_obstacle_release < 0:
                self.release_obstacle(elapsed_time)
                self.time_till_next_obstacle_release = random.uniform(3, 10)  # TODO Change bounds with time

            # -- Scoop Generation -- #
            # Decrement scoop release timer
            if self.time_till_next_scoop_release > 0:
                self.time_till_next_scoop_release -= 1 / self.FPS
            # Check if timer has reached zero
            if self.time_till_next_scoop_release < 0:
                self.release_scoop()
                self.time_till_next_scoop_release = random.uniform(1, 6)  # TODO Change bounds with time


            self.cone.update_state(1/self.FPS)
            self.background.update_state(elapsed_time)
            if self.background.did_reach_end():
                self.message_to_screen("You Win!", self.WHITE, self.WINDOW_WIDTH / 3, self.WINDOW_HEIGHT / 3)
                pygame.display.update()
                return 0  # Wait for user to exit

            # Draw everything
            pygame.display.update()  # updates the screen (for every run through the loop)
            self.background.draw(self.screen)
            for scoop in self.falling_scoops:
                scoop.draw(self.screen)
            for obstacle in self.all_obstacles:
                obstacle.draw(self.screen)
            self.cone.draw(self.screen)

            # Display score
            self.message_to_screen('Score: %i' % self.score, self.BLUE, 10, 10)

            self.clock.tick(self.FPS)  # Pause to maintain the given frame rate

    def release_obstacle(self, time_elapsed):
        """ Release an obstacle appropriate for the given time into the game

            :param time_elapsed: number of seconds elapsed during the game
        """
        # Calculate background position
        y = self.BG_CHANGE_SPEED_SCALAR * math.pow(time_elapsed, self.BG_CHANGE_SPEED_EXP)
        thresholds = [700*x for x in range(len(self.OBSTACLE_TYPES))]

        obs_type = self.OBSTACLE_TYPES[0]
        for i in range(len(thresholds)-1, -1, -1):
            if y > thresholds[i]:
                obs_type = self.OBSTACLE_TYPES[i]
                break

        rand_x_loc = random.randint(0, self.WINDOW_WIDTH)

        if obs_type == Leaf.__class__:
            obs = Leaf(rand_x_loc, 0)
        elif obs_type == Bee.__class__:
            obs = Bee(rand_x_loc, 0)
        elif obs_type == Drone.__class__:
            obs = Drone(rand_x_loc, 0)
        elif obs_type == Balloon:
            obs = Balloon(rand_x_loc, 0)
        elif obs_type == Asteroid.__class__:
            obs = Asteroid(rand_x_loc, 0)
        else:
            raise Exception('Invalid obstacle type: %s' % obs_type)

        obs.rect.bottom = -1  # Place just above top of screen
        self.all_obstacles.append(obs)

    def release_scoop(self):
        """ Release a falling ice cream scoop """
        rand_x = random.randint(0, self.WINDOW_WIDTH)
        scoop = Scoop(rand_x, 0)
        scoop.rect.bottom = -1  # Place just above top of screen
        self.falling_scoops.append(scoop)


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
