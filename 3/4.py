
#zad 4

import math
def sortByDistWithSort(lista):
    lista.sort(key=lambda x: math.sqrt((x[0]**2)+(x[1]**2)))

def sortByDistWithSorted(lista):
   return sorted(lista,key=lambda x: math.sqrt((x[0]**2)+(x[1]**2)))

lista = [(12,48),(45,2),(0,2),(0,3),(1,8)]
print("Sortowanie przez sorted tworzy nowa liste i nie przeprowadza zmian na liscie oryginalnej")
print(sortByDistWithSorted(lista))
print(lista)
print("***********")
print("Sortowanie przez sort operuje na oryginalnej liscie i dokonuje nad niej zmian")
print(sortByDistWithSort(lista))
print(lista)

