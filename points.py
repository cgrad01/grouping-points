class Point(object):
  def __init__(self, lat, lon, id):
    self.lat = lat
    self.lon = lon
    self.id = id

test = Point(33,21,"a1b2c3")

print test.id