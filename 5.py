import sys
#filename = sys.argv[1]
filename = str(input())
sysArg = str(input())
if filename == '-':
    for line in sys.stdin:
        if line == 'exit\n':
            sys.stdin.close()
            break
        #elif sys.argv[2] in line:
        elif sysArg in line:
            print("Znaleziono: "+line)
    
else:
    try:
        f = open(filename,"rt")
        string = f.readlines()
        for line in string:
            #if sys.argv[2] in line:
            if sysArg in line:
                print(line.strip())
        f.close()
    except:
        print("Blad: ", sys.exc_info())
