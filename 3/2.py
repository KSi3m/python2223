
#zad 2
def generator(n):
        a, b = 0, 1
        while n:
            n -= 1
            a, b = b, a + b
            yield a

print([x for x in generator(20)])

