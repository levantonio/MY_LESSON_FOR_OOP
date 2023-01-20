class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    # @classmethod  # метод класса!!!!!!!!!!
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left  # Меняем атрибут класса 'MIN_COORD' извне!!!!!!!!!!!

    # pt = Point(12, 54)
    # pt.set_bound(-98)
    # print(Point.__dict__) # 'MIN_COORD': -98!!!!!!!!!!!!!!

    # методы для атрибутов
    # __setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса
    # __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
    # __getattr__(self, item) - автоматически вызывается при получении несуществующего item класса
    # __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно существует оно или нет)

    def __getattribute__(self, item):
        print('__getattrubute__')
        if item == "y":
            raise ValueError("Доступ запрещён")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError(f" {key} -> Недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('__getattr__' + ' атрибута - ' + item + "--> не существует")

    def __delattr__(self, item):
        print('__gelattr__' + ' атрибут - ' + item + "--> удалён")
        object.__delattr__(self, item)  # Гарантированно удаляет атрибут(del pt.x) -например


pt = Point(54, 454)  # выведет __getattrubute__
# a = pt.x
# b = pt.y # Вызовет ошибку - доступ запрещён
# print(a)  # -выведет 54
# pt.z = 87  # Вызовет ошибку - "z -> Недопустимое имя атрибута"

