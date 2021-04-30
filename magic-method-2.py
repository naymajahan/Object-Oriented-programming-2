
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f'Point2D({self.x, self.y})'




    def __str__(self):
        return f'class: Point2D, ' \
               f' x: {self.x}, y: {self.y}'


    def __add__(self, other):
        if isinstance(self, other.__class__):
            return Point2D(self.x + other.x, self.y + other.y)
        else:
            return None

    def __sub__(self, other):
        if isinstance(self, other.__class__):
            return Point2D(self.x - other.x, self.y - other.y)
        else:
            return None



    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.x == other.x and self.y == other.y



    def __ne__(self, other):
        if isinstance(self, other.__class__):
            return self.x == other.x or self.y == other.y



    def __lt__(self, other):
        if isinstance(self, other.__class__):
            return self.x < other.x or (self.x == other.x and self.y < other.y)


    def __hash__(self):
        return hash(self.x + self.y)



p1 = Point2D(1, 2)
p2 = Point2D(2, 3)
p6 = Point2D(1, 2)


#print(p1)
#print(repr(p1))
#print(str(p1))


p3 = p1 + p2
print(p3)

p4 = p1 -p2

print(p4)


#print(p1 == p6)
#print(p1 is p6)


print(p1 != p2)
print(p1 != p6)

print(p1 < p2)

print(p1 < p6)

point_set = set()

point_dic = dict()

point_set.add(p1)
print(point_set)

