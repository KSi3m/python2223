#zad 1
import math
class LiczbaZespolona:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def __repr__(self):
        rep = str(self.__a)+" + "+str(self.__b)+"i"
        return rep

    def __add__(self, other):
        return LiczbaZespolona(self.__a+other.__a,self.__b+other.__b)

    def __sub__(self, other):
        return LiczbaZespolona(self.__a - other.__a, self.__b - other.__b)

    def __mul__(self, other):
        return LiczbaZespolona((self.__a * other.__a)-(self.__b * other.__b), (self.__b * other.__a)+(self.__a * other.__b))

    def __truediv__(self, other):
        return LiczbaZespolona(((self.__a * other.__a) + (self.__b * other.__b))/(other.__a**2 + other.__b**2),
                        ((self.__b * other.__a) - (self.__a * other.__b))/(other.__a**2 + other.__b**2))

    def module(self):
        return math.sqrt((self.__a**2)+(self.__b**2))

    def checkIfEqual(self,other):
        if self.__a == other.__a and self.__b == other.__b:
            return True
        return False

a = LiczbaZespolona(12,5)
b = LiczbaZespolona(3,2)
c = LiczbaZespolona(3,2)
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(b.module())
#print(a.checkIfEqual(b))
#print(b.checkIfEqual(c))

#zad 2
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