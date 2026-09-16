import math
from abc import ABC, abstractmethod


class Figure(ABC):
    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("figure must be a Figure class")
        return self.area + figure.area

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, side_a:int, side_b:int):
        if side_a <=0 or side_b <= 0:
            raise ValueError("side_a and side_b must be positive")

        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return ((self.side_a + self.side_b) * 2)


class Square(Rectangle):
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError("side_a must be positive")
        super().__init__(side_a, side_a)


        self.side_a = side_a


class Triangle(Rectangle):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        if (side_a >= side_b + side_c) or (side_b >= side_a + side_c) or (side_c >= side_b + side_a):
            raise ValueError("Len of side must be less than sum of others")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return(self.side_a + self.side_b + self.side_c)

    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))




class Circle(Rectangle):
    def __init__(self, radius:float):
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius * self.radius)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius




r = Rectangle(10, 5)
s = Square(5)
t = Triangle(5, 5, 5)
c = Circle(5)
print(r.add_area(c))





