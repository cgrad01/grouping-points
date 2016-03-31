from points import Point
from route import Route
points = Point.instantiate(Point.parse_json("points.json"))

# Latitudes range from -90 to 90.
# Longitudes range from -180 to 180.

test = Route()

print test.center_point.id