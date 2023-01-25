class Point2D:
    __slots__ = ('x', 'y')
    """ __dict__ - работать не будет. и имена в экземплярах можно указывать только указанные в __slots__
    сейчас __slots__ = ('x', 'y') значит имена в экземплярах можно указывать x, y"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # @property  # Это будет геттер
    # def length(self):
    #     return self.__length
    #
    # @length.setter
    # def length(self, value):
    #     self.__length = value
    #


class Point3D(Point2D):
    # __slots__ = () можно явно передать ссылку на колекцию слотс из базового класса + + + можно указать добавочные свойства
    # __slots__ = 'z', - запятая в конце - обязательна!!!
    # def __init__(self, x, y, z):
    #     super().__init__(x, y)
    #     self.z = z
    pass


p = Point3D(10, 25)
print(p.__dict__)  # __slots__ не передается при наследовании, но можно указать явно!!!!
