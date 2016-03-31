from points import Point
import random

class Route(object):
  def __init__(self):
    self.ref_point = self.make_random_point()

  def make_random_point(self):
    random_lat = random.uniform(-90, 90)
    random_lon = random.uniform(-180, 180)
    return Point(random_lat, random_lon, "mid_one")


