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

  def run_grouper(self, group_amount, filename):
    grouper = Grouper(group_amount, filename)
    grouper.get_each_dist()
    grouper.assign_group_members()
    grouper.adjust()
    grouper.write_groups()