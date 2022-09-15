import math
from math import pi

earth_radius = 6371000000

def cube_volume(x,y,z):
    lego_volume = x*y*z
    return lego_volume


def earth_volume(earth_radius):
    planet_volume = (4/3)*pi*(earth_radius**3)
    return planet_volume


def how_many():
    x = cube_volume(16,16,10)
    y = earth_volume(earth_radius)

    nr = y/x
    return nr


print(how_many())

