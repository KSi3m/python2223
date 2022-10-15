import sys

def fun(filename,req):
    if filename == '-':
        for line in sys.stdin:
            if line == 'exit\n':
                sys.stdin.close()
                break
            elif req in line:
                print("Znaleziono: "+line)
        
    else:
        try:
            f = open(filename,"rt")
            string = f.readlines()
            for line in string:
                if req in line:
                    print(line.strip())
            f.close()
        except:
            print("Blad: ", sys.exc_info())

if len(sys.argv) > 2:
    filename = sys.argv[1]
    req = sys.argv[2]
    fun(filename,req)
else:
    print("Zbyt mao argumentow")