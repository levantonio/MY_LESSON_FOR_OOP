try:
    x, y = map(int, input("Введите значения x и y").split())
    try:
        res = x / y
    except ZeroDivisionError as z:  # каждый раз имя можно указывать одно и тоже - а оно будет только для определенного as
        print(f"Ошибка деления на '0' --> {z}")
except ValueError as z:
    print(f"Некорректное значение типа данных -->1 {z}")
else:
    print("Не произошло никаких исключений")
finally:  # неапример, для закрытия файла при ошибке
    """
    with open("eekjhf.txt") as f: --> всегда файл будет закрыт
    """
    print("Finally произойдет всегда!!!!!!")
