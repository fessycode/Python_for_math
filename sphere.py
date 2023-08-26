#!/usr/bin/python3
"""
The module print out the volume and the surface area of sphere
"""
import math

def volume_area_sphere(radius):
    """ To calculate the volume """
    volume = (4/3) * math.pi * radius**3

    """ To calculate the surface area"""

    surface_area = 4 * math.pi * radius**2
    return volume, surface_area
