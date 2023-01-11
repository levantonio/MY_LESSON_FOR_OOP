class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y): #метод
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)




pt = Point()
pt2 = Point()
pt2.set_coords(10, 20)
pt.set_coords(1, 2)
print(pt.x) #print(pt.__dict__) либо так
print(pt.y)
print(pt2.__dict__)
print(pt.get_coords())

print(getattr(pt, 'get_coords'))

