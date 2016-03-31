from points import Point
from route import Route

class Grouper(object):
  def __init__(self, num_of_routes, filename):
    self.num_of_routes = num_of_routes
    self.routes = self.make_routes(self.num_of_routes)
    self.filename = filename
    self.points = Point.instantiate(Point.parse_json(self.filename))

  def calc_distances(self, points):
    distances = []
    for point in points:
      distances.append(route.center_point.get_distance(point))
    distances.sort()
    return distances

  def make_routes(self, num_of_routes):
    routes = []
    for i in range(num_of_routes):
      routes.append(Route())
    return routes
