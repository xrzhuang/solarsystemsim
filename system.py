__author__ = 'MaxZhuang'
from math import sqrt
from body import Body

GRAVITATIONAL_CONSTANT = 6.67384e-11

# System object class
class System:

    # constructor
    def __init__(self, body_list):
        self.body_list = body_list

    # method to compute acceleration of single index in list
    def compute_acceleration(self, n):
        ax = 0
        ay = 0

        # for loop for every other object in index
        for i in range(0, len(self.body_list)):
            if i != n :

                # calculation of acceleration in x and y
                dx = self.body_list[i].get_x() - self.body_list[n].get_x()
                dy = self.body_list[i].get_y() - self.body_list[n].get_y()
                radius = sqrt( (dx * dx) + (dy * dy) )
                total_acceleration_n = (self.body_list[i].get_mass() * GRAVITATIONAL_CONSTANT)/(radius * radius)
                ax_i = total_acceleration_n * (dx/radius)
                ay_i = total_acceleration_n * (dy/radius)
                ax = ax + ax_i
                ay = ay + ay_i
        # returns calculation
        return (ax, ay)

    # method to update velocity and position of body objects in system
    def update(self, timestep):

        # calculation using compute_acceleration for every body object in the system
        for n in range(0, len(self.body_list)):
            (ax_n, ay_n) = self.compute_acceleration(n)
            self.body_list[n].update_velocity(ax_n, ay_n, timestep)
            self.body_list[n].update_position(timestep)

    # draws every object using for loop for list of body objects
    def draw(self, cx, cy, pixels_per_meter):
        for i in range (0, len(self.body_list)):
                self.body_list[i].draw(cx, cy, pixels_per_meter)

