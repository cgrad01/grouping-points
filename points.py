import json
import math

points = []
pairs = []
class Point(object):

  def __init__(self, lat, lon, id):
    self.lat = lat
    self.lon = lon
    self.id = id

  @classmethod
  def instantiate(cls,parsed_data):
    for entry in parsed_data:
      point = Point(entry["lat"], entry["lon"], entry["id"])
      points.append(point)
    return points

  @classmethod
  def parse_json(cls,file):
    with open(file) as data:
      parsed_points = json.load(data)
      return parsed_points

  def get_distance(self, destination):
    lat_difference = self.lat - destination.lat
    lon_difference = self.lon - destination.lon
    return math.sqrt(lat_difference**2 + lon_difference**2)
