from point import Point
import random
# The Group class is initialized with a reference point, by which all other points are compared to. It is responsible for adding Group members (points), and creating reference points.

class Group(object):

  def __init__(self):
    self.ref_point = self.make_ref_point()
    self.members = []

  def make_ref_point(self):
    random_lat = random.uniform(-90, 90)
    random_lon = random.uniform(-180, 180)
    return Point(random_lat, random_lon, "ref_point")

  def add_member(self, point):
    self.members.append(point)

  def get_new_ref(self):
    self.ref_point = self.make_ref_point()