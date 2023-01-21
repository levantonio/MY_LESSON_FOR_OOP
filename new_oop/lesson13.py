"""__str__() - для отображения информации об объекте класса для пользователей (например, для функций print, str)"""
"""__repr__() - для отображения информации об объекте класса в режиме отладки (для разработчиков)"""
"""__len__() - позволяет применить функцию len() к экземплярам класса"""
"""__abs__() - позволяет применить функцию abs() к экземплярам класса"""


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}" # вывод, для отладки
#
#     def __str__(self): # Вывод, для пользователя
#         return f"{self.name}"


# cat = Cat("Васька")
# print(cat)

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):  # для вызова функции len, для экземпляра класса
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(12, -32)
print(p.__dict__)
print(len(p))  # Функцию len() можно вызвать только с определением метода в классе
print(abs(p))
