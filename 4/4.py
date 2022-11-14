

def print_tree(exc, ind):
    print("+"*ind + exc.__name__)
    for x in exc.__subclasses__():
        print_tree(x,ind+3)
        
        
print_tree(BaseException,0)