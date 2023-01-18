class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod  # декоратор!!!!!!!!!!   метод класса!!!!!!! Работает только с атрибутами класса
    def validate(cls, arg):  # метод класса!!!!!!!
        return cls.MIN_COORD <= arg <= cls.MAX_COORD  # вернёт True или False это работает только с атрибутами класса

    # с атрибутами экземпляра класса это не работает так как нет !!!!!  self  !!!! cls-> Ссылка на сам класс!

    def __init__(self, x, y):  # Конструктор
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):  # Если х или у вне диапазона значения будут == 0!!
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))  # можно передать параметры из экземпляра класса

    def get_coord(self):  # Метод
        return self.x, self.y

    @staticmethod  # Статический метод работает независимо от класса
    def norm2(x, y):  # переменные берутся не из класса, а явно передаются при вызове
        return x * x + y * y


v = Vector(10, 2)
res = Vector.get_coord(v)
res1 = v.get_coord()
print(res, '\n', res1)
print(Vector.validate(99))  # вернёт True или False
r = Vector(1, 120)
print(r.get_coord())  # Будет (0, 0)
print(Vector.norm2(5, 7))
