"""
---> исключения в момент исполнения
---> исключения при компиляции(до исполнения кода)
"""

try:
    f = open("test.txt")
except FileNotFoundError:  # Код ошибки
    print("Файл не найден")
print("программа работает далее")

try:
    a = 2 / 0
except ZeroDivisionError:  # можно сколько угодно except прописывать, либо через запятую либо по иерархии выше т.е
    """
    Exception                  
        |
    ArithmeticError и др...
        |
    ZeroDivisionError и др...
    """
    print("На ноль делить нельзя")
print("программа работает далее")
