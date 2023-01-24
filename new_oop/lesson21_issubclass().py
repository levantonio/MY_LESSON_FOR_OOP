""" Наследование от встроенных функций """


class Geom:
    pass


class Circle(Geom):
    pass


g = Geom()
c = Circle()
print(issubclass(Circle, Geom))  # True Проверка наличия класса и наследования от встроенных функций


class Vector(list):  # list если не переопределять __str__ то вывод будет[1,2,3]
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)  # 1 2 3
