class Cat:  # Создали класс котов
    name = None
    age = None
    isHappy = None

    def __init__(self, name = None, age = None, isHappy = None): # Конструктор
        # self.name = name
        # self.age = age
        # self.isHappy = isHappy
        self.set_data(name, age, isHappy)

        self.get_data()



    def set_data(self, name = None, age = None, isHappy = None): #SELF - по умолчанию
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print("name:", self.name, ", age:", self.age, ", happy?:", self.isHappy)



cat1 = Cat("bars", 3, True)  # экземпляр класса
#cat1.set_data("bars", 3, True)
#cat1.get_data()
#cat1.get_data()


cat2 = Cat("jopen", 2, False)  # экземпляр класса
#cat2.set_data("jopen", 2, False)


cat3 = Cat("laps", 2) # для этого указал значения по умолчанию None в конструкторе и методе
cat1 = Cat("pirog") #  для этого указал значения по умолчанию None в конструкторе и методе
cat1 = Cat() # из за значений по умолчанию- можно вызывать cat1 - сколько егодно раз, передавая значения в скобках
# cat1.get_data()
# cat2.get_data()


