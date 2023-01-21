class TreadData:
    __shared_attrs = {
        "name": "thread1",
        "data": {},
        "id": 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs  # обращение экземпляра класса к локальным свойствам класса


th1 = TreadData()
th2 = TreadData()
th2.id = 3
print(th1.__dict__)  # изменили свойство атрибута в классе
