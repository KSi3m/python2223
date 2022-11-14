import subprocess
out=''

try:
    out = subprocess.run(["dir"], shell=True)
except subprocess.CalledProcessError as e:
    print(e.output)

