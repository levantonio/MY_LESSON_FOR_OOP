# def create_class_point(name, base, attrs):
#     attrs.update({"MAX_COORD": 100, "MIN_COORD": 0})
#     return type(name, base, attrs)
class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs.update({"MAX_COORD": 100, "MIN_COORD": 0})
        return type.__new__(cls, name, bases, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coord(self):
        return (0, 0)


pt = Point()
print(pt.get_coord())
print(pt.MAX_COORD)
