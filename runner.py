from points import Point

points = Point.instantiate(Point.parse_json("points.json"))
a = points[0]
b = points[1]
print a.get_distance(b)