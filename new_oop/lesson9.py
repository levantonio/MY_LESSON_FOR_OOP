class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property  # декораторами прописали код закомментированный ниже
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):  # Имена методов - должны совпадать!!!!!!!
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old
    # old = property(get_old, set_old)  # удобней так считывать и записывать информацию
    # # или!!!!!!
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)


p = Person("Сергей", 20)
# p.set_old(35)
# print(p.get_old())
print(p.old)
a = p.old = 359  # через property задали переиенную old и через нее обращаемся к сеттерам и геттерам
print(a)
o = Person("Анна", 23)
print(p.__dict__)
print(o.__dict__)
p.old = 5
print(p.__dict__)
