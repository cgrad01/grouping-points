from points import Point
from route import Route

points = Point.instantiate(Point.parse_json("points.json"))
route = Route()

distances = []
for point in points:
  distances.append(route.center_point.get_distance(point))
distances.sort()
print distances