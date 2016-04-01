from point import Point
import random

class Group(object):
  def __init__(self, id):
    self.ref_point = self.make_ref_point()
    self.members = []
    self.id = id
  def make_ref_point(self):
    random_lat = random.uniform(-90, 90)
    random_lon = random.uniform(-180, 180)
    return Point(random_lat, random_lon, "ref_point")

  def add_member(self, point):
    self.members.append(point)

  # WONT WORK UNTIL YOU FINISH DEALING WITH POINTS

  # def get_ref_point_distances(self):
  #   results = []
  #   for ref_point in self.ref_points:
  #     results.append(self.calc_distances(ref_point))
  #   return results

  # def calc_distances(self, ref_point):
  #   distances = {}
  #   for point in self.points:
  #     distances[point.id] = ref_point.get_distance(point)
  #   return distances

