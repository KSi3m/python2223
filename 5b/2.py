import subprocess
out=''

dirStr1='''
K1
_K2
_K3
__K4
K5
_K6
'''
dirStr2='''
K1
_K2
_K3
__K4
___K5
__K6
___K7
__K8
_K9
_K10
K11
_K12
__K13
'''
def fun(dirStr):
    kek = dirStr.strip().split("\n")
    output = ""
    arr = []
    currLevel = 0
    for x in range(len(kek)):
        if kek[x].startswith("K"):
            arr.append(kek[x])
            output = kek[x]
            currLevel = 0
            continue
            
        if kek[x].count('_') > currLevel:
            output += "\\"+kek[x][kek[x].count('_')::]
            arr.append(output)
            currLevel += 1
            continue
        
        if kek[x].count('_') == currLevel:
            output = output[:output.rfind('\\'):]
            output += "\\"+kek[x][kek[x].count('_')::]
            arr.append(output)
            continue
            
        if kek[x].count('_') < currLevel:
            for a in range(currLevel - kek[x].count('_')+1):
                output = output[:output.rfind('\\'):]
            output += "\\"+kek[x][kek[x].count('_')::]
            arr.append(output)
            currLevel = kek[x].count('_')
            continue
            
    xd = " ".join(arr)
    #print(xd)
    try:
        out = subprocess.run("mkdir "+xd, shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError) as ex:
        print(ex)
    


fun(dirStr2)