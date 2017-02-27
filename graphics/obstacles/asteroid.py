from graphics.obstacles.obstacle import Obstacle


class Asteroid(Obstacle):

    def __init__(self):
        """ Initializes a new Scoop object at the given position and scale.

            x_pos: int - the x-coordinate of the top-left corner
            y_pos: int - the y-coordinate of the top-left corner
            scale: int - scales the size of the scoop
        """
        Obstacle.__init__(self)


    def update_state(self, dt):
        # TODO Update the location of the asteroid
        pass
