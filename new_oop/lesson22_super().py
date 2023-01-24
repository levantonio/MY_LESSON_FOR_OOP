class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f" инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):  # расширение базового класса или переопределение, если в базовом классе есть такой метод

    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):  # super() - возвпащает ссылку на базовый класс(self писать не надо)
        super().__init__(x1, y1, x2, y2)  # вызвали инициализатор от класса родителя(убрали дублирование кода)
        print("Инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")


l = Line(1, 2, 3, 4)  # будет вызван инициализатор line, а если его нет, то вызван инициализатор geom
print(l.__dict__)

r = Rect(9, 8, 7, 4, 9)
print(r.__dict__)
