class Decc():

    liss = []
    def __init__(self,fun):
        self.fun = fun
        
    def __call__(self,*args):
        self.liss.append((self.fun.__name__,self.fun(*args)))
        return self.fun(*args)
   
    def print_list(self):
        for x in self.liss:
            print(x)
        
        
@Decc
def ret(x,y):
    return x+y
    
@Decc
def srr(x,y):
    return str(x)+" "+str(y)
    
@Decc
def kek(*args):
    sum = ""
    for x in args:
        sum += str(x)
    return sum
    
print(ret(12,12))
print(ret(34,55))
print(ret(77,78))
print(srr(77,78))
print(srr("aa",78))
print(ret(77,78))
print(srr("aaaa","bbbb"))
print(kek("aaaa","bbbb",111111, "125" ,"aaabvc"))
D = Decc(Decc)
D.print_list()

    
        
  
        
        
        
        
        
