#созадть класс MyPoint (x,y) любой чтобы он считал расстояние от поинта ло поинта который заходит через параметры и считаетсяч через корень
#Евклидовая тема как я поняла и сама формула под корнем (х2-х1)
#добавь класс майпоинт 3д который наследуется от майпоинта но добавляет значение z и переписать метод инит
import math

class MyPoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other_point) -> float:
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)

point1 = MyPoint(0, 0)
point2 = MyPoint(5, 5)
print(f"from {point1.x} to {point2.x} = {point1.distance_to(point2)}")
class MyPoint3D(MyPoint):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self.z = z

    def distance_to(self, other_point) -> float:
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2 + (other_point.z - self.z) ** 2) ** 0.5

point1_3d = MyPoint3D(0, 0, 0)
point2_3d = MyPoint3D(6, 4, 5)
distance_3d = point1_3d.distance_to(point2_3d)

print(f"from {point1_3d.x} to {point2_3d.y} = {point1_3d.distance_to(point2_3d)}")