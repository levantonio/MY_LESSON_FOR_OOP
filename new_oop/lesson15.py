# Методы сравнений!!!!!!!!!!!!!!!!
# __eq__() = ==
# __ne__() = !=
# __lt__() = <
# __le__() = <=
# __gt__() = >
# __ge__() = >=

class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod  # вынесли закомментированный ниже код в отдельный метод, что бы не  было дублирующего кода!!!!!!!!
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError(" правый операнд должен быть int или Clock!!!!!!!!")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        # if not isinstance(other, (int, Clock)):
        #     raise TypeError(" правый операнд должен быть int или Clock!!!!!!!!")
        #
        # sc = other if isinstance(other, int) else other.seconds
        sc = self.__verify_data(other)
        return self.seconds == sc  # автоматом работает "==" и "!="

    def __lt__(self, other):
        # if not isinstance(other, (int, Clock)):
        #     raise TypeError(" правый операнд должен быть int или Clock!!!!!!!!")
        #
        # sc = other if isinstance(other, int) else other.seconds
        sc = self.__verify_data(other)
        return self.seconds < sc  # автоматом работает "<" и ">"

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc  # автоматом работает "<=" и ">="


c1 = Clock(1000)
c2 = Clock(17000)
print(c1 == c2)
print(c1 < c2)
