"""__add__() - для операции сложения"""
"""__sub__() - для операции вычитания"""
"""__mul__() - для операции умножения"""
"""__truediv__() - для операции деления"""


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):  # т.е текущий экземпляр класса + other (1000 + other)
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(" правый операнд должен быть int или Clock!!!!!!!!")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other  # 100 + c1

    def __iadd__(self, other):
        print('__iadd__')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(" правый операнд должен быть int или Clock!!!!!!!!")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self


c1 = Clock(1000)
c2 = Clock(2000)
c3 = c1 + c2
print(c3.get_time())
print(c1.__dict__)
