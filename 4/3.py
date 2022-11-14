import re

class InvalidPesel(Exception): 
    def __init__(self):
        pass
    
    def __str__(self):
        return "Nieprawidlowy pesel"
        
class InvalidName(Exception): 
    def __init__(self):
        pass
    
    def __str__(self):
        return "Nieprawidlowe imie/nazwisko"
        


class Osoba:

    def __init__(self,imie,nazwisko,pesel):
        self.set_imie(imie)
        self.set_nazwisko(nazwisko)
        self.set_pesel(pesel)


    def set_imie(self,imie):
        valid = re.match(r'^[\w]+$',imie)
        if valid:
            self.imie = valid.group()
        else: raise InvalidName()
            
    def set_nazwisko(self,nazwisko):
        valid = re.match(r'^[\w]+$',nazwisko)
        if valid:
            self.nazwisko = valid.group()
        else: raise InvalidName()


    def set_pesel(self,pesel):
        pat = re.compile(r'''^(?P<rok>\d{2})
        (?P<miesiac>\d{2})
        (?P<dzien>\d{2})
        (?P<reszta>\d{3})
        (?P<plec>\d)
        (?P<suma_kontrolna>\d)$''',re.IGNORECASE | re.VERBOSE)

        valid = re.match(pat,pesel)
        if valid:
            dik = {}
            wagi_sumy = [1,3,7,9,1,3,7,9,1,3]
            
            if int(valid.group(2)) in range(1,13) or int(valid.group(2)) in range(21,33): pass
            else: raise InvalidPesel()
            
            suma = 0
            for k in range(len(valid.group(0))-1):
                temp = int(valid.group(0)[k]) * wagi_sumy[k]
                suma += temp
            if 10-(suma%10) == int(valid.group(6)): self.pesel = pesel
            else: raise InvalidPesel()
        else: raise InvalidPesel()
    
    def __str__(self):
        return self.imie+" "+self.nazwisko+" "+self.pesel


try:
    o = Osoba("Jose","Mourinho","81010200141")
except InvalidName as e:
    print(e)
except InvalidPesel as e:
    print(e)
else:
    print(o)
