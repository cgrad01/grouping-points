from point import Point
from group import Group
from grouper import Grouper

class Controller(object):

  def get_group_amount(self):
    while True:
      try:
        group_amount = int(raw_input("Input number of desired groups: "))
      except ValueError:
        print "Please input a valid integer."
      else:
        break
    return group_amount

  def get_filename(self):
    return raw_input("Input full name of input file: ")

controller = Controller()
grouper = Grouper(controller.get_group_amount(), controller.get_filename())
grouper.get_each_dist()
grouper.assign_group_members()
grouper.adjust()
grouper.write_groups()
