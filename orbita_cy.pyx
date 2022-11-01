#from libc.math cimport sqrt
cdef extern from "math.h":
    double sqrt(double x)
    
cdef class Planet(object):
    cdef public double x,y,z,vx,vy,vz,m
    def __init__(self):
        #some initial position and velocity
        self.x = 1.0
        self.y = 0.0
        self.z = 0.0
        self.vx = 0.0
        self.vy = 0.5
        self.vz = 0.0

        # some mass
        self.m=1.0

cdef void single_step(planet,double dt):
    """Make a single time step"""
    #Compute force: gravity towards origin
    cdef double distance = sqrt(planet.x**2 + planet.y**2 + planet.z**2)
    cdef double Fx= -planet.x/distance**3
    cdef double Fy= -planet.y/distance**3
    cdef double Fz= -planet.z/distance**3

    #Time step position, according to velocity
    planet.x += dt * planet.vx
    planet.y += dt * planet.vy
    planet.z += dt * planet.vz

    #Time step velocity, according to force and mass
    
cdef void step_time(planet, double time_span, int n_steps):
    """Make a number of time steps forward"""
    cdef double dt = time_span / n_steps

    for j in range (n_steps):
        single_step(planet, dt)

def main():
    Planeta_ = Planet()
    step_time(Planeta_, 5000,10000000)
