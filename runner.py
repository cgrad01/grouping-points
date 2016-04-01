from point import Point
from group import Group
from grouper import Grouper

test = Grouper(3, "points.json")
test.pass_groups()
test.assign_group_members()
for group in test.groups:
  print len(group.members)
test.adjust()

for group in test.groups:
  print len(group.members)

for point in test.groups[0].members:
  print point.id, point.dist_to_refs
