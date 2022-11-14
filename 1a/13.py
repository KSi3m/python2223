def pierwiastki_trojmianu(a,b,c):
    if a <= 0:
        return "blad"
    d = b**2 - 4*a*c
    if d < 0:
        return "brak znakow"
    if d == 0:
        return -b/(2*a)
    else:
        return [-b+d/(2*a),-b-d/(2*a)]
        
 
print(pierwiastki_trojmianu(45,8,9))
print(pierwiastki_trojmianu(5,7,1))
print(pierwiastki_trojmianu(0,8,9))