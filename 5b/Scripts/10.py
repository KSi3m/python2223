def wypisz(n):
    for x in range(1,n):
        if x%4 == 0 or x%9 == 0:
            print(x)
        
        
wypisz(sys.argv[1])
wypisz(78)