from accessify import private, protected


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.__x = x
        self.__y = y

    @private  # защитили доступ к методу
    @classmethod
    def check_value(sls, x):
        return type(x) in (int, float)  # True/False

    # атрибуты без подчеркиваний - имеют публичный доступ
    # атрибуты с щдним нижним подчеркиванием(_х) - имеют доступ protected - для обращения внутри класса и в дочерних классах
    # атрибуты с двумя нижними подчеркиваниями(__х) - имеют доступ private - для обращения только внутри класса и в дочерних классах

    def set_coord(self, x, y):  # Сеттер!!!!!!!
        if self.check_value(x) and self.check_value(y):  # Проверка в !!!@classmethod!!!
            self.__x = x
            self.__y = y
        else:
            raise ValueError('координаты должны быть числами')

    def get_coord(self):  # Геттер!!!!!!!
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())
pt.check_value(5)  # защитили доступ извне
