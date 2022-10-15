import sys

def wc(filename):
    try:
        f = open(filename,'rt')
        lines = f.readlines()
        words = []
        for x in lines:
            words.extend(x.strip().split())

        chars = "".join(words)
        
        print("Wiersze "+str(len(lines)))
        print("Słowa "+str(len(words)))
        print("Znaki "+str(len(chars)))

        f.close()
    except:
        print("Blad: ", sys.exc_info())
        
 

#filename = "m.txt"    
if len(sys.argv) > 1:
    filename = sys.argv[1] 
    wc(filename)
else:
    print("Zbyt malo argumentow")
       
     
