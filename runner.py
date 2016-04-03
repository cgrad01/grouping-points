from point import Point
from group import Group
from grouper import Grouper

# TODOs:
# Implement command line functionality
# gets(raw_input("Input the number of groups you would like: "))

test = Grouper(5, "points.json")
test.pass_groups()
test.assign_group_members()
for group in test.groups:
  print len(group.members)
test.adjust()

for group in test.groups:
  print len(group.members)

for group in test.groups:
  for point in group.members:
    print point.id, point.dist_to_refs
  print "BREAK"
