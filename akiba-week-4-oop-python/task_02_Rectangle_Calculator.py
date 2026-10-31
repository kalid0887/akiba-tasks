class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return (self.height * self.width)

    def calculate_perimeter(self):
        return (self.height * 2) + (self.width * 2)


rectangle1 = Rectangle(4, 6)
rectangle1 = Rectangle(7, 5)

print(f"the area of rectangle 1 is {rectangle1.calculate_area()}")
