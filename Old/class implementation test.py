class Shape:
    def calcArea(self):
        print("calculating area")
class Rectangle(Shape):
    def calcArea(self):
        print("area of rect = lenght * breadth")
class triangle(Shape):
    def calcArea(self):
        print("area of triangle  = 0.5 * lenght * breadth")
class Circle(Shape):
    def calcArea(self):
        print("area of circle = 3.14 * radius * radius")

shapes = [Rectangle(), triangle(), Circle()]
for shape in shapes:
    shape.calcArea()