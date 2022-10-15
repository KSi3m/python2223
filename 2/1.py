
def dict_fun(string):
    dic = {}
    x = string.split("\n")
    for i in range(3):
        p = x[i].strip().split(":")
        dic[p[0]] = p[1]
    print(dic)
 


ss = '''tttt:125
jjjj:3456
tyt:7893 ''' 
dict_fun(ss)
