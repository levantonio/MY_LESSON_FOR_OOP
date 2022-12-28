class Bulding:
    __year = None
    __city = None  # __ Это пример инкапсуляции

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("year: ", self.year, "city: ", self.city)


class School(
        Bulding):  # Это наследование, тут есть все от класса Bulding + можно изменять функции, под School или прописывать новое

    pupils = 0  # типа ученики в школе

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)  # Автозаполнением запихалось
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        # полиморфизм - преписанная или дополненная функция, для определенного класса наследника
        print("pipuls: ", self.pupils)



class House(Bulding):  # Это наследование, тут есть все от класса Bulding + можно изменять функции, под House или прописывать новое
    rooms = 0

    def __init__(self, rooms, year, city):
        super(House, self).__init__(year, city)
        self.rooms = rooms
        
    def get_info(self):
        super().get_info()
        print(f"in the house = {self.rooms} rooms")


class Shop(Bulding):  # Это наследование, тут есть все от класса Bulding + можно изменять функции, под Shop или прописывать новое
    pass


school = School(100, 2000, "Moscow")
house = House(4, 2000, "Moscow")
shop = Bulding(2000, "Moscow")

school.get_info()
house.get_info()
