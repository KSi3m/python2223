def wypisz_do_listy(n):
    res = []
    for x in range(1,n):
        if x%3 == 0 or x%7 == 0:
            res.append(x)
    return res    
        
print(wypisz_do_listy(45))
print(wypisz_do_listy(78))