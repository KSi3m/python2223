import sys

def cp(original,copy):
    try:
        with open(original, "rb") as f_1:
            with open(copy, "wb") as f_2:
                byte = f_1.read(1)
                while byte:
                    f_2.write(byte)
                    byte = f_1.read(1)
                    
    except:
         print("Blad: ", sys.exc_info())
         
         

if len(sys.argv) > 2:
    original = sys.argv[1]
    copy = sys.argv[2]
    cp(original,copy)
else:
    print("Zbyt malo argumentow")


