import math


class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        area = self.side**2

        return round(area, 2)

    def diagonal(self) -> float:
        diagonal = math.sqrt(self.side**2 + self.side**2)

        return round(diagonal, 2)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
