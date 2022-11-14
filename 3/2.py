import re

def url_path_to_dict(path):
    pattern = (r'^'
               r'((?P<protokol>.+?)://)?'
               r'(?P<adres_domenowy>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<parametry>[?].*?)?'
               r'(?P<kotwica>#.*?)?'
               r'$'
               )
    regex = re.compile(pattern)
    m = regex.match(path)
    d = m.groupdict() if m is not None else None

    return d

def zad2(filename):
    with open(filename, encoding="utf-8") as f:
        linie = f.read()
        
        regexUrl = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        
        url = re.findall(regexUrl,linie)      
        linie = [x[0] for x in url]
            
        pattern = (r'^'
               r'((?P<protokol>.+?)://)?'
               r'(?P<adres_domenowy>.*?)'
               r'(:(?P<port>\d+?):)?'
               r'(?P<path>/.*?)?'
               r'(?P<parametry>[?].*?)?'
               r'(?P<kotwica>#.*?)?'
               r'$'
               )
        regex = re.compile(pattern)


        for x in linie:
            m = regex.match(x)
            d = m.groupdict() if m is not None else None
            print(d)

  
zad2("plik_urle.txt")