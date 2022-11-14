import re

def join_tuple_string(strings_tuple) -> str:
   return ''.join(strings_tuple)

def zad1(filename):
    with open(filename, encoding="utf-8") as f:
        linie = f.read()
        print(linie)
        regex1 = r"([1-9]|1[0-9]|2[0-9]|3[0-1])( )(IX|IV|V?I{0,3}|X?I{0,2})(\.| )(19[0-9][0-9]|20[0-9][0-9])"
        regex2 = r"([1-9]|1[0-9]|2[0-9]|3[0-1])(\.)(0[1-9]|1[0-2])(\.)(19[0-9][0-9]|20[0-9][0-9])"
        regex3 = r"([1-9]|1[0-9]|2[0-9]|3[0-1])( )(stycznia|lutego|marca|kwietnia|maja|czerwca|lipca|sierpnia|wrzesnia|pazdziernika|listopada|grudnia)( )(19[0-9][0-9]|20[0-9][0-9])"
        matches = []
        for x in (regex1,regex2,regex3):
            matches += re.findall(x,linie)

        result  = map(join_tuple_string,matches)
        print(list(result))
        
        
zad1("plik_daty.txt")