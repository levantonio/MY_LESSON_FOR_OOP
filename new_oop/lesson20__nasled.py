class Geom:  # Базовай класс
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):  # в скобочках прописали родительский класс
    name = "Line"  # переопределяем название атрибута

    def draw(self):
        print("Рисуем линию")


class Rect(Geom):  # в скобочках прописали родительский класс
    def draw(self):
        print("Рисуем прямоугольник")


l = Geom()
print("l.name = ", l.name)
l.set_coords(1, 2, 3, 4)
print(l.__dict__)
