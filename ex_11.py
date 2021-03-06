class Circle:
    def __init__(self, r):
        import math
        self.pi = math.pi
        self.rds = r

    def area(self):
        return (self.rds**2) * self.pi

    def draw(self):
        import turtle as t
        t.circle(self.rds)
        t.exitonclick()
        

class Triangle:
    def __init__(self, a, b, angle):
        from math import radians, sin
        self.a = a
        self.b = b
        self.angle = angle
        self.sin = sin(radians(angle))

    def area(self):
        return (1/2) * self.a * self.b * self.sin

    def draw(self):
        import turtle as t
        t.forward(self.a)
        t.left(180 - self.angle)
        t.forward(self.b)
        t.setposition(0,0)
        t.exitonclick()
        
class Hexagon:
    def __init__(self, a):
        self.side = a

    def area(self):
        hexa = Triangle(self.side, self.side, 60)
        return hexa.area() * 6

    def draw(self):
        import turtle as t
        for i in range(6):
            t.forward(self.side)
            t.left(60)
        t.exitonclick()
    
