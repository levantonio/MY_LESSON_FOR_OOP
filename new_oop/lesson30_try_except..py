def func2():
    return 2 / 0


def func1():
    return func2()


"""
исключения можно обрабатывать на любом уровне ошибок 
"""

try:
    func1()
except:
    print("func1 error")
