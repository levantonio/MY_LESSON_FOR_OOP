class Goods:
    def __init__(self, name, weight, price):
        super().__init__()  # Вызов class MixonLog
        print("Initialized Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"Name: {self.name}, Weight: {self.weight}, Price: {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("Initialized MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00.00 часов")

    def print_info(self):
        print("print_info: из класса MixinLog")


class Notebook(Goods, MixinLog):  # Порядок имеет значение!!!!!!

    # def print_info(self):
    #     MixinLog.print_info(self)


n = Notebook("Acer", 5.2, 3000)
n.print_info()  # вызовется из базового класса Goods
n.save_sell_log()
MixinLog.print_info(n)  # вызов из класса MixinLog либо в классе переопределить метод, как закоментированный
# n.print_info() будет вызываться из класса MixinLog из переопределенного метода
