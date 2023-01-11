class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y): #можно тут явно указать значения х  и у === инициализатор
        print("Вызов __init__")
        self.x = x #х и у - в создании экземпляоа класса нужно явно прописывать аргументы
        self.y = y

    def __del__(self):
        print('удаление экземпляра')  #финализатор

    def set_coords(self, x, y): #метод
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point(1, 2)
print(pt.__dict__)


