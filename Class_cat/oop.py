class Cat:  # Создали класс котов
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy): #SELF - по умолчанию
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print("name:", self.name, ", age:", self.age, ", happy?:", self.isHappy)



cat1 = Cat()  # экземпляр класса
cat1.set_data("bars", 3, True)
cat1.get_data()
# cat1.name = "bars"
# cat1.age = 3
# cat1.isHappy = True

cat2 = Cat()  # экземпляр класса
cat2.name = "jopen"
cat2.age = 2
cat2.isHappy = False
cat2.get_data()

# print(cat1.name)
# print(cat2.name)