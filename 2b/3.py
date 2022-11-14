class Kolo:
    def __init__(self,diameter,use):
        self.__diameter = diameter
        self.__use = use
        
    def setDiameter(self, newDiameter):
        self.__diameter = newDiameter
        
    def setUse(self, newUse):
        self.__use = newUse
        
    def getInfo(self):
        d = {}
        d['diameter'] = self.__diameter
        d['use'] = self.__use
        if hasattr(super(), 'getInfo'): 
            d.update(super().getInfo())    
        return d
class Silnik:
    def __init__(self,power,strokes):
        self.__power = power
        self.__strokes = strokes
    
    def setStrokes(self, newStrokes):
        self.__strokes = newStrokes
        
    def setPower(self, newPower):
        self.__power = newPower

    def getInfo(self):
        d = {}
        d['power'] = self.__power
        d['strokes'] = self.__strokes
        if hasattr(super(), 'getInfo'): 
            d.update(super().getInfo()) 
        return d
        
class Skrzynia:
    def __init__(self,transmission,parts):
        self.__transmission = transmission
        self.__parts = parts
    
    def setTransmission(self, newTransmission):
        self.__transmission = newTransmission
        
    def setParts(self, newParts):
        self.__parts = newParts
    
    def getInfo(self):
        d = {}
        d['transmission'] = self.__transmission
        d['parts'] = self.__parts
        if hasattr(super(), 'getInfo'): 
            d.update(super().getInfo()) 
        return d
        
class Samochod(Kolo,Silnik,Skrzynia):
    def __init__(self,diameter='-',use='-',power='-',strokes='-',transmission='-',parts='-',colour='-',typeOf='-'):
        Kolo.__init__(self,diameter,use)
        Silnik.__init__(self,power,strokes)
        Skrzynia.__init__(self,transmission,parts)
        self.__colour = colour
        self.__typeOf = typeOf
        
    def setColour(self, newColour):
        self.__colour = newColour
        
    def setType(self, newType):
        self.__typeOf = newType
        
    def getInfo(self):
        d = {}
        d['colour'] = self.__colour
        d['type'] = self.__typeOf
        if hasattr(super(), 'getInfo'): 
           d.update(super().getInfo()) 
        return d

def printResult(dict):
    for key, value in dict.items():
        print(key, ' : ', value) 
    print('----------------------')

a = Samochod(18,"Zimowe","75 KM",4,"Manual",5,"Zielony","Sedan")
b = Samochod()
printResult(a.getInfo())
printResult(b.getInfo())
b.setDiameter(19)
printResult(b.getInfo())


