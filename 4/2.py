import re

class BadIpAdrress(Exception): 
    def __init__(self):
        pass
    
    def __str__(self):
        return "Nieprawidlowy adres ip"
        
class BadPCName(Exception): 
    def __init__(self):
        pass
    
    def __str__(self):
        return "Nieprawidlowa nazwa"
        
class BadNetmask(Exception): 
    def __init__(self):
        pass
    
    def __str__(self):
        return "Nieprawidlowa maska sieciowa"
      

class IpConfig:

    def __init__(self,pc_name,ip,mask):
        self.set_pc_name(pc_name)
        self.set_ip(ip)
        self.set_mask(mask)
        
    def set_pc_name(self,pc_name):
        valid = re.match(r'^[\w\-]+$',pc_name)
        if valid:
            self.__pc_name = valid.group()
            #print(self.__pc_name)
        else:
            raise BadPCName()

        
    def set_ip(self,ip):
        valid = re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[^0-9]?[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',ip)
        if valid:
            self.__ip = valid.group()
            #print(self.__ip)
        else:
            raise BadIpAdrress()
    def set_mask(self,mask):
        valid = re.match(r'^(?:/[1-2][0-9]|/3[0-2]|/[0-9][^0-9])$',mask)
        if valid:
            self.__mask = valid.group()
        else:
            raise BadNetmask()
            
    def __str__(self):
        return self.__pc_name+" "+self.__ip+self.__mask
        
  
try:
    i = IpConfig("Komputer-Osobisty","123.25.68.128","/28")
except BadPCName as e:
    print(e)
except BadIpAdrress as e:
    print(e)
except BadNetmask as e:
    print(e)
else:
    print(i)
