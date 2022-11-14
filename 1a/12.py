def fib(n):
    if (n<=1):
        return n
    return fib(n-2) + fib(n-1)
    
n = 20    
print([fib(x) for x in range(1,n)])