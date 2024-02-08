class Shape:
    def __init__(self):
        self.Area = 0

class Rectangle(Shape):
    def __init__(self, Length, Width):
        super().__init__()
        self.Length = Length
        self.Width = Width

    def calculate_area(self):
        return self.Length * self.Width * 2

a = Rectangle(12, 6)
print(a.calculate_area())
