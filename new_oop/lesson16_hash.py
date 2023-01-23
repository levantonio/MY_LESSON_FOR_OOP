# Если обьекты a == b (равны), то равен и их hash!!!!!!!!!!!!
# Равные хэши: hash(a) == hash(b) не гарантируют иавенство обьектов
# Если хэши не равны hash(a) != hash(b), то обьекты точно не равныe

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


pt1 = Point(1, 2)
pt2 = Point(1, 2)

print(hash(pt1), hash(pt2), sep="\n")

d = {}
d[pt1] = 1
d[pt2] = 2
print(d)
