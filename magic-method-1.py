
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f'Point2D({self.x, self.y})'




    def __str__(self):
        return f'class: Point2D, ' \
               f' x: {self.x}, y: {self.y}'




p1 = Point2D(1, 2)
p2 = Point2D(2, 3)

print(p1)
print(repr(p1))
print(str(p1))


