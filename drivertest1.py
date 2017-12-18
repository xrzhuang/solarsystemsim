__author__ = 'MaxZhuang'
# import classes and cs1lib
from cs1lib import *
from system import System
from body import Body


# set constants to be used
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
TIME_SCALE = 100000         # how many real seconds for each second of simulation
PIXELS_PER_METER = 3 / 1e7  # distance scale for the simulation
EARTH_MASS = 5.9736e24  # real mass of Earth
MOON_MASS = 7.3477e22
MOON_X = 3.484403e8
MOON_VY = 1022
FRAME_RATE = 30             # frames per second
TIMESTEP = 1.0 / FRAME_RATE # time between drawing each frame


# main function of driver
def main():

    # creates objects
    earth = Body(EARTH_MASS, 0, 0, 0, 0, 24, 0, 0, 1)            # blue earth
    moon = Body(MOON_MASS, MOON_X, 0, 0, MOON_VY, 4, 1, 1, 1)   # white moon
    earth_moon = System([earth, moon])

    # cs1lib functions
    set_clear_color(0, 0, 0)    # black background
    enable_smoothing()

    # while loop that runs as long as the window is open
    while not window_closed():
        clear()

        # draws earth and moon using the system class draw method, divide by 2 for center
        earth_moon.draw(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, PIXELS_PER_METER)
        earth_moon.update(TIMESTEP * TIME_SCALE)

        # Draw the frame and take a brief nap.
        request_redraw()
        sleep(TIMESTEP)

# actually running the function
start_graphics(main, "Earth-moon simulation", WINDOW_WIDTH, WINDOW_HEIGHT)
