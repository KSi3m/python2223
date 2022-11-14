import subprocess
import glob

files = []
for file in glob.glob(".\\Scripts\\*.py"):
    files.append(file)


ok = []
notOk = []
#print(files)
for x in files:
    try:
        out = subprocess.run(["python",x], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)
        ok.append(x)
    except subprocess.CalledProcessError as e:
        notOk.append(x)
        #print(e.output)



print(ok)
print(notOk)
