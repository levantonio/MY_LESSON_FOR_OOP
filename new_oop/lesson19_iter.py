# __iter__(self) получение итератора для перебора обьекта
# __next__(self) переход к следующему значению, для его считывания

class RRange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):  # теперь можно перебрать список циклом for
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:  # value- текущее значение итерации
            self.value += self.step
            return self.value

        else:
            raise StopIteration


fr01 = RRange(0, 2, 0.5)
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
for i in fr01:
    print("*", i, "*")
print("*" * 180)


class Frange2D:
    def __init__(self, start=0.0, stop=0.0, step=0.0, rows=5):
        self.rows = rows
        self.fr = RRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr02 = Frange2D(0, 2, 0.5, 4)
for row in fr02:
    for i in row:
        print(i, end=" ")
    print()
