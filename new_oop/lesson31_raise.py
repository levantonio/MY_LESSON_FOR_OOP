# print("Я к вам пишу — чего же боле?")
# print("Что я могу еще сказать?")
# print("Теперь, я знаю, в вашей воле")
#
# raise ZeroDivisionError("искусственно вызванная ошибка")
#
# print("Меня презреньем наказать.")
# print("Но вы, к моей несчастной доле")
# print("Хоть каплю жалости храня,")
# print("Вы не оставите меня.")

class ExceptionPrintSendData(Exception):
    """Класс исключения при отправке принтеру"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"***Ошибка: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"Печать {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("Принтер не отвечает")  # ==self.message

    def send_to_print(self, data):
        return False


p = PrintData()
p.print("1, 2, 3")
# try:
#     p.print("1, 2, 3")
# except ExceptionPrintSendData:
#     print("принтер не овечает")
