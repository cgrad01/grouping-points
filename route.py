from points import Point
import random

class Route(object):
  def __init__(self):
    self.stops = []
    self.center_point = self.make_random_point()
  def make_random_point(self):
    random_lat = random.uniform(-90, 91)
    random_lon = random.uniform(-180, 181)
    mid_point = Point(random_lat, random_lon, "mid_one")
    return mid_point
