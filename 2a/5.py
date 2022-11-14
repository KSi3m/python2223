
#zad 5
import os

generator5= (x for x in os.listdir(os.getcwd()) if x.endswith(".py"))

for x in generator5:
    print(x)
