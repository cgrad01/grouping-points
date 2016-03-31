from points import Point
from route import Route
from grouper import Grouper

# points = Point.instantiate(Point.parse_json("points.json"))
# route = Route()

test = Grouper(3, "points.json")
for distance in test.calc_distances()[0]:
  print distance

print "BREAK"

for distance in test.calc_distances()[1]:
  print distance

print "BREAK"

for distance in test.calc_distances()[2]:
  print distance