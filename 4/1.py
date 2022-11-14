import re
class EmailException(Exception): 
    def __init__(self):
        pass
    
    def __str__(self):
        return "Nieprawidlowy adres email"
      


class Email:
    def __init__(self,mail):
        if self.validate(mail) is False:
            raise EmailException()
        else:
            print(mail)
    def validate(self,mail): 
        pattern = re.compile(r'[a-zA-Z0-9._\+" "!%-]+@[a-zA-Z0-9._-]+|(\.[a-zA-Z._-]+)')
        #pattern = re.compile(r'[\w\.]+@[\w\.]+') #wersja uproszczona
        match = re.match(pattern,mail)
        return True if match else False
      

adresy = ['simple@example.com','very.common@example.com','disposable.style.email.with+symbol@example.com','other.email-with-hyphen@example.com','user.name+tag+sorting@example.com','Abc.example.com']


for x in adresy:
    try:
        g = Email(x)
    except EmailException as e:
        print(e)

