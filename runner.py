from points import Point
from grouper import Grouper

# points = Point.instantiate(Point.parse_json("points.json"))
# route = Route()

test = Grouper(2, "points.json")
for group in test.groups:
  for point in test.points:
    group.add_member(point)

for group in test.groups:
  for point in test.points:
    point.dist_to_refs[group.id] = point.get_distance(group.ref_point)

print test.points[0].dist_to_refs








# calcs = test.get_ref_point_distances()[0]
# for key in calcs:
#   print key, calcs[key]

# print "BREAK"

# ref_min = min(calcs.values())
# for key in calcs:
#   if calcs[key] == ref_min:
#     print key, calcs[key]


# for distance in test.calc_distances()[1]:
#   print distance

# print "BREAK"

# for distance in test.calc_distances()[2]:
#   print distance