import json
class Point(object):

  def __init__(self, lat, lon, id):
    self.lat = lat
    self.lon = lon
    self.id = id
  @classmethod
  def instantiate(cls,parsed_data):

  @classmethod
  def parse_json(cls,file):
    with open(file) as data:
      parsed_points = json.load(data)
      return parsed_points

Point.parse_json("points.json")