class ReadIntX:  # Дескриптор, для считывания данных
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:  # дескриптор данных (с геттерами и сеттерами)

    @classmethod
    def verify_coord(cls, coord):  # проверка на то, что координата являетя числом - иначе будет ошибка
        if type(coord) != int:
            raise ValueError("Введите целое число")

    def __set_name__(self, owner, name):  # owner-> ссылка нв сам класс integer name -> имя (x или y или z)
        self.name = "_" + name  # пример: name = _x
        print("*" * 20)

    def __get__(self, instance, owner):  # Геттер
        return getattr(instance, self.name)  # instance ->ссылка на экземпляр класса owner-> Ссылка на класс Point

    def __set__(self, instance, value):  # Сеттер
        self.verify_coord(value)
        print(
            f"__set__:  {self.name} = {value}")  # instance->ссылка на экземпляр класса value->значение экземпляра класса
        setattr(instance, self.name, value)  # сработает столько раз, сколько переменных в экземпляре класса


"""Есть дескрипторы данных и дескрипторы не данных(они могут только считывать информацию)"""


class Point3D:
    x = Integer()  # обращение к дескриптору(класс integer)
    y = Integer()  # это и есть дескриптор
    z = Integer()  # типа класс в классе
    xr = ReadIntX()  # Дескриптор неданных!!!!!!!!!!!!!!!!

    def __init__(self, x, y, z):
        self.x = x  # Обращаемся напрямую к сеттерам и геттерам
        self.y = y  # и если проверка не пройдена в @classmethod -> данные не запишутся
        self.z = z  # Убрали нижнее подчёркивание!!!!!!!!!


p = Point3D(1, 2, 3)
print(p.__dict__)
p.z = 20
print(p.__dict__)
print(p.xr)  # выведет 1

# ********************
# ********************
# ********************
# __set__:  _x = 1
# __set__:  _y = 2
# __set__:  _z = 3
# {'_x': 1, '_y': 2, '_z': 3}
# __set__:  _z = 20
# {'_x': 1, '_y': 2, '_z': 20}
