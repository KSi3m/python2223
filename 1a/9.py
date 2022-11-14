def inst(a,b,c):
    if isinstance(a,str):
        print(str(type(a))+" "+a)
    if isinstance(b,int):
        print(str(type(b))+" "+str(b))
    if isinstance(c,float):
        print(str(type(c))+" "+str(c))
    
inst('a',185,12.456)