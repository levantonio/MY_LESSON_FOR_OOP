from colorama import *

print(Fore.GREEN)


# class Point:
#     def __new__(cls, *args, **kwargs):
#         print(f'Вызов __new__ для {str(cls)}')
#         return super().__new__(cls) # Ворачиваем адрес нового созданного обьекта
#
#     def __init__(self, x=0, y=0):
#         print(f'Вызов __init__ для {str(self)}')
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# print(pt)


class DataBase:
    __instanse = None

    def __new__(cls, *args, **kwargs):  # Что бы экземпляр класса был создан только один и не был перезаписан
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)

        return cls.__instanse

    def __del__(self):
        DataBase.__instanse = None  # Вернули предыдущие данные экзеипляру класса

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data):
        print(f'Запись в Бд из {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '12234', 8220)
print(db.psw, db2.psw)  # доказательство, что экземпляр класса нельзя переопределить
