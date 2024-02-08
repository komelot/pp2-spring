class Shape:
    def __init__(self):
        self.Area = 0

    def area(self):
        return self.Area


class Square(Shape):
    def __init__(self, Length):
        super().__init__()
        self.Length = Length
        self.Area = Length ** 2

a = Square(10)
b = Shape()
print(a.Area)
print(b.Area)
