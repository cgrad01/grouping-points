from point import Point
from group import Group
import random

class Grouper(object):
  def __init__(self, num_of_groups, filename):
    self.num_of_groups = num_of_groups
    self.filename = filename
    self.points = Point.instantiate(Point.parse_json(self.filename))
    self.groups = []
    self.make_groups(self.num_of_groups)

  def make_groups(self, num_of_groups):
    for i in range(num_of_groups):
      self.groups.append(Group())

  def assign_group_members(self):
    for point in self.points:
      self.groups[point.get_min_index()].add_member(point)