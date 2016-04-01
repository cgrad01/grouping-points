from point import Point
from grouper import Grouper

test = Grouper(3, "points.json")

for group in test.groups:
  for point in test.points:
    point.dist_to_refs.append(point.get_distance(group.ref_point))

test.assign_group_members()

for group in test.groups:
  print len(group.members)

for point in test.groups[0].members:
  print point.id, point.dist_to_refs
