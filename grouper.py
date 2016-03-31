from points import Point
from route import Route
import random

class Grouper(object):
  def __init__(self, num_of_groups, filename):
    self.num_of_groups = num_of_groups
    self.filename = filename
    self.points = Point.instantiate(Point.parse_json(self.filename))
    self.ref_points = self.make_random_points(self.num_of_groups)

  def make_random_points(self, num_of_points):
    ref_points = []
    for i in range(num_of_points):
      random_lat = random.uniform(-90, 90)
      random_lon = random.uniform(-180, 180)
      ref_points.append(Point(random_lat, random_lon, "ref_point"))
    return ref_points

  def get_ref_point_distances(self):
    results = []
    for ref_point in self.ref_points:
      results.append(self.calc_distances(ref_point))
    return results

  def calc_distances(self, ref_point):
    distances = {}
    for point in self.points:
      distances[point.id] = ref_point.get_distance(point)
    return distances

  def make_routes(self, num_of_routes):
    routes = []
    for i in range(num_of_routes):
      routes.append(Route())
    return routes
