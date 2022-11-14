import sys

def fun(key):
    try:
        with open("plik3.txt","rt") as f:
            string = f.readlines()
            dic = {}

            for line in string:
                line = line.strip().split(': ')
                print(line)
                dic[line[0]] = line[1]
        
            print(dic[key])
    except:
        print("Bład: ", sys.exc_info())
     
fun('k1')
fun('k3')