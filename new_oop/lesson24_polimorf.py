"""Полиморфизм- это воозможность работы с совершенно разными
обьектами (языка PYTHON) единым образом!!!!!!!!!!!!!!!!!!!!!!!!"""


class Geom:
    def get_pr(self):  # называется абстрактом()
        raise NotImplementedError("В дочернем классе должен быть определен метод get_pr()")


class Rectangle(Geom):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_pr(self):  # называем методы единым именем потому что ссылка на обьект ведет к его классу
        return 2 * (self.width + self.height)


class Square(Geom):
    def __init__(self, side):
        self.side = side

    def get_pr(self):  # называем методы единым именем потому что ссылка на обьект ведет к его классу
        return 4 * self.side


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):  # называем методы единым именем потому что ссылка на обьект ведет к его классу
        return self.a + self.b + self.c


"""Что бы не забыть поставить методы единым именем как вариант создать класс- содержащий исключение!!! """

geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)
        ]

for i in geom:
    print(i.get_pr())
