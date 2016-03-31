from points import Point
from route import Route
from grouper import Grouper

# points = Point.instantiate(Point.parse_json("points.json"))
# route = Route()

test = Grouper(2, "points.json")
print test.routes
print len(test.points)