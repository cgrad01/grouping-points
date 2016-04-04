from grouper import Grouper
# The Controller communicates information from the user, to the Grouper module, which then distributes the necesarry information to the subclasses. The Controller also validates user input is within certain constraints.
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
    while True:
      try:
        filename = raw_input("Input full name of input file: ")
        with open(filename) as data:
          print "File found"
      except IOError:
        print "Sorry, we could not find that file, confirm it exists in this directory, and that you include the file extension when inputting."
      else:
        break
    return filename

  def run_grouper(self, group_amount, filename):
    grouper = Grouper(group_amount, filename)
    grouper.get_each_dist()
    grouper.assign_group_members()
    grouper.adjust()
    grouper.write_groups()