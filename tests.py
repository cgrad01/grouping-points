from point import Point
from group import Group
from grouper import Grouper

# point tests
test_point_one = Point(50.00000, 100.00000, "test1")
test_point_one.dist_to_refs = [1,2,0]
test_point_two = Point(0.000000, 50.000000, "test2")
test_point_two.dist_to_refs = [1,0,2]

print "Point test 1"
if type(test_point_one.lat) == type(1.00000):
  result = True
else:
  result = False
print "   Point has a float 'lat' attribute: " + str(result)

print "Point test 2"
if type(test_point_one.lon) == type(1.00000):
  result = True
else:
  result = False
print "   Point has a float 'lon' attribute: " + str(result)

print "Point test 3"
if type(test_point_one.id) == type("string"):
  result = True
else:
  result = False
print "   Point has an string 'id' attribute: " + str(result)

print "Point test 4"
if type(test_point_one.get_distance(test_point_two)) == type(1.00000):
  result = True
else:
  result = False
print "   Point has a get_distance method that takes a point, and returns a float: " + str(result)

print "Point test 5"
if test_point_one.get_distance(test_point_one) == 0.00000:
  result = True
else:
  result = False
print "   #get_distance returns a distance of zero when comparing a point to itself: " + str(result)

print "Point test 6"
if type(test_point_one.get_min_index()) == type(1):
  result = True
else:
  result = False
print "   Point has a get_min_index method that returns an integer: " + str(result)

print "Point test 7"
if test_point_one.get_min_index() == 2 and test_point_two.get_min_index() == 1:
  result = True
else:
  result = False
print "   #get_distance returns a the index of the smallest value in the 'dist_to_refs' attribute: ", result