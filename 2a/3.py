
#zad 3
def fun_log(a):
    if a%3==0 and a%7==0:
        return True
    return False

def filterr(fun,lista):
    return [x for x in lista if fun(x)]

print(filterr(fun_log,[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]))

