from point import Point
from grouper import Grouper

# points = Point.instantiate(Point.parse_json("points.json"))
# route = Route()

test = Grouper(3, "points.json")

for group in test.groups:
  for point in test.points:
    point.dist_to_refs.append(point.get_distance(group.ref_point))

for point in test.points:
  test.groups[point.dist_to_refs.index(min(point.dist_to_refs))].add_member(point)

for group in test.groups:
  print len(group.members)

for point in test.groups[0].members:
  print point.id, point.dist_to_refs
