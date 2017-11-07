import subprocess
from glob import glob



files=glob('*.ps')

print files

for f in files:
	result = subprocess.check_call(['ps2eps',f])
