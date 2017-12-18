__author__ = 'MaxZhuang'
# import cs1lib
from cs1lib import *

# Body object class
class Body:

    # constructor
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    # updates position of object
    def update_position(self, timestep):
        self.x = (self.vx * timestep) + self.x
        self.y = (self.vy * timestep) + self.y

    # updates the velocity of object
    def update_velocity(self, ax, ay, timestep):
        self.vx = (ax * timestep) + self.vx
        self.vy = (ay * timestep) + self.vy

    # draws object using cs1lib functions, setting color given by parameters, draws circle by using given position multipled by pixels per meter and centering
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x * pixels_per_meter + cx, self.y * pixels_per_meter + cy, self.pixel_radius)

    # getters
    def get_mass(self):
        return self.mass

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y



