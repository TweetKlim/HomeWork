import math

class Circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.w * self.l
		
radius = int(input("radius"))
circle = Circle(radius)
print(circle.area(), circle.perimeter())

length = int(input("length"))
width = int(input("width"))
rec = Rectangle(length,width)
print(rec.area())