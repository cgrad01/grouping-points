from point import Point
from group import Group
import json
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

  def pass_groups(self):
    for group in self.groups:
      self.get_dist_to_ref(group)

  def get_dist_to_ref(self, group):
    for point in self.points:
        point.dist_to_refs.append(point.get_distance(group.ref_point))

  def assign_group_members(self):
    for point in self.points:
      self.groups[point.get_min_index()].add_member(point)

  def reset_groups(self):
    for group in self.groups:
      group.members = []

  def get_group_index(self, group):
    return self.groups.index(group)

  def update_dist_to_ref(self, group):
    for point in self.points:
      point.dist_to_refs[self.get_group_index(group)] = point.get_distance(group.ref_point)

  def adjust(self):
    count = 0
    for group in self.groups:
      if len(group.members) == 0:
        group.get_new_ref()
        self.reset_groups()
        self.update_dist_to_ref(group)
        self.assign_group_members()
        count +=1
        self.adjust()

  def groups_to_dict(self):
    output = {}
    for group in self.groups:
      output[self.groups.index(group)] = [x.id for x in group.members]
    return output


  def write_groups(self):
    with open('groups.json', 'w') as outfile:
      json.dump(self.groups_to_dict(), outfile)

# FIGURE OUT HOW TO DO THIS
  # def write_output(self):

