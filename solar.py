__author__ = 'MaxZhuang'

from cs1lib import *
from system import System
from body import Body

# set Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 5000000         # how many real seconds for each second of simulation
PIXELS_PER_METER = 7e-10  # distance scale for the simulation
FRAME_RATE = 30             # frames per second
TIMESTEP = 1.0 / FRAME_RATE # time between drawing each frame

# main function
def main():

    # create body objects
    sun = Body(1.98892e30, 0, 0, 0, 0, 25, .7, .7, 0)  # sun with real mass and variables for simulation
    mercury = Body(3.285e23, 5.79e10, 0, 0, 47890, 3 ,.3, .3, .3)  # mercury with real mass, location, and velocity for simulation
    venus = Body(4.867e24, 1.082e11, 0, 0, 35040, 7.65, .8, .4, 0)  # venus with real mass, location, and velocity for simulation
    earth = Body(5.972e24, 1.49598e11, 0, 0, 29790, 7.98, 0, 0, 1)  # earth with real mass, location, and velocity for simulation
    mars = Body(6.39e23, 2.2798e11, 0, 0, 24140, 4.32, 1, 0, 0)  # mars with real mass, location, and velocity for simulation

    # create system object
    solar = System([sun, mercury, venus, earth, mars ])

    # create settings
    set_clear_color(0, 0, 0)    # black background
    enable_smoothing()

    # while loop when window is open
    while not window_closed():
        clear()

        # draw the system in its current state.
        solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

        # update the system for its next state.
        solar.update(TIMESTEP * TIME_SCALE)

        # draw the frame and take a brief nap.
        request_redraw()
        sleep(TIMESTEP)

# runs graphics
start_graphics(main, "Earth-moon simulation", WINDOW_WIDTH, WINDOW_HEIGHT)