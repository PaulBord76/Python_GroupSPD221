class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        distance = ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        return distance


point1 = Point(1, 2)
point2 = Point(4, 6)

distance_between_points = point1.dist(point2)
print(distance_between_points)