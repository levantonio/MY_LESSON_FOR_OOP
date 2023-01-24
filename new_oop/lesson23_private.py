class Geom:
    name = "Geom"
    """к приватным атрибутам и методам можно обращатся только оттуда, откуда они определены"""

    def __init__(self, x1, y1, x2, y2):
        print(f" инициализатор Geom для {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):  # Нельзя использовать __атрибут в дочерних классах, либо убрать одно подчеркивание
        return (self.__x1, self.__y1)


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill="red"):  # super() - возвпащает ссылку на базовый класс(self писать не надо)
        super().__init__(x1, y1, x2, y2)  # вызвали инициализатор от класса родителя(убрали дублирование кода)
        self.__fill = fill


r = Rect(10, 20, 30, 40)
print(r.__dict__)
r.get_coords()
