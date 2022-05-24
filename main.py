#!/usr/bin/env python

from objects import *

from shapely.geometry import Point
from datetime import datetime



def main():
        p = Programmer(id=0, first_name="Lauren", last_name="Champlin", years_of_experience=4)
        print(p.id)
        return 0



main()