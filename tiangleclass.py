import math 

class Triangle():
    def __init__(self,a,b,c):
        self.adj1 = a
        self.adj2 = b
        self.hypo = c 

    def perimeter(self):
        return self.adj1 + self.adj2 + self.hypo

    s = perimeter

    def area(self):
        return sqrt(s * (s - self.adj1) * (s - self.adj2) * (s - self.hypo))

    def scale(self, scale_factor):
        return Triangle(scale_factor * self.adj1, scale_factor * self.adj2, scale_factor * self.hypo


t = Triangle(3,4,5)

print("Perimeter = %d" % t.perimeter())
print("Area = %d" % t.area())

q = t.scale(2)
print(q.adj1, q.adj2, q.hypo)
q.area()

