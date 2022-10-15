import math
class Punkt2D:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __sub__(self, other):
        return math.sqrt(((other.a-self.a)**2)+((other.b-self.b)**2))


r = Punkt2D(18,98)
t = Punkt2D(0,9)
print(r-t)

class Punkt3D(Punkt2D):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c

    def __sub__(self, other):
        return math.sqrt(((other.a-self.a)**2)+((other.b-self.b)**2)+((other.c-self.c)**2))

y = Punkt3D(18,98,14)
u = Punkt3D(0,9,32)

print(y-u)