# __getitem__(self,item) - Получение значения по ключу item
# __setitem__(self,key, value) - запись значения по ключу key
# __delitem__(self,key) - удаление элемента по ключу key

class Student:
    def __init__(self, name, marks):  # marks - список оценок
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):  # получаем список по индексу
        if 0 <= item and item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым, неотрицательным числом")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)  # увеличиваем размер списка до неправильного списка
            self.marks.extend([None] * off)  # в несуществующих индексах до доюавленного будет сформирован None
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым, неотрицательным числом")

        del self.marks[key]


s1 = Student('Sergei', [4, 5, 3, 5, 5, 5, 4])
print(s1.__dict__)
print(s1[2])  # синтаксис из за метода __getitem__
s1[0], s1[10] = 1, 9
print(s1.__dict__)
del s1[2]
print(s1.__dict__)
