class Point: # определяем класс
    "_Класс, для определения точек на плосkости_" # строка __doc__
    color = 'red' #атрибут или свойство класса/ переменная
    circle = 2

# Point.color = "black"
print(Point.__dict__) # смотрим, что есть в классе поинт - какие свойства, методы и др.

a = Point() # Экземпляр класса имеющий атрибут color и circle
b = Point() # Экземпляр класса имеющий атрибут color и circle

a.circle = 10 # изменил локальное значение, для этого экземпляра класса
# или
setattr(Point, 'prop', 1) # добавление нового атрибута в пространство имен point
print(getattr(Point, "prop")) # выдаст False если такого атрибута не существует в point или вернёт значение атрибута
print(hasattr(Point, 'prop')) # проверяет существует ли данный атрибут в point и выдаёт true или false
print(a.prop)
delattr(Point, 'prop') # Удалили атрибут  из класса point
print(hasattr(Point, 'prop')) # проверяет существует ли данный атрибут и выдаёт true или false


print(a.circle)
print(a.__dict__)
print(b.circle)
delattr(a, 'circle')
print(a.__dict__)
print(a.circle)

a = Point()
b = Point()
a.x = 1
a.y = 2

b.x = 10
b.y = 20

print(Point.__doc__)


