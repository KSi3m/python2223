import re

def test_if_valid(address,netmask):
    ip = address.split(".")
    netmask = netmask.split(".")

    for x,y in zip(ip,netmask):
        if int(x) & int(y) == int(x): continue
        else: return False
    return True
    

def zad3(filename):
 
    with open(filename) as f:
        linie = f.read()
        print(linie)
        slash = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|[^0-9]?[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:/[1-2][0-9]|/3[0-2]|/[0-9][^0-9])')
        normal = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) (?:(?:0|128|192|224|240|248|252|254|255)\.){3}(?:0|128|192|224|240|248|252|254|255)?')
 
        ips = slash.findall(linie)
        nor = normal.findall(linie)
        
        for i in ips:
            k = i.split('/')
            netmask = '.'.join([str((0xffffffff << (32 - int(k[1])) >> i) & 0xff) for i in [24, 16, 8, 0]])
            if test_if_valid(k[0],netmask):
                print('/'.join(k))
            
        for i in nor:
            k = i.split(' ')
            if test_if_valid(k[0],k[1]):
                print(' '.join(k))
     

        
    
  

zad3("plik_adresy_IP.txt")