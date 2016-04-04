import json
from haversine import haversine

points = []
class Point(object):

  def __init__(self, lat, lon, id):
    self.lat = lat
    self.lon = lon
    self.id = id
    self.dist_to_refs = []

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
    return haversine((self.lat, self.lon), (destination.lat, destination.lon))

  def get_min_index(self):
    return self.dist_to_refs.index(min(self.dist_to_refs))

  def to_json(self):
    return self.id