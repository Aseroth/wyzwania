import math
from math import pi

one_rad = 180/pi

def to_radian(radian: float):
    to_deg = radian * one_rad

    return to_deg


print(to_radian(0.05))
