
#Author : Senthilkumar Lakshmanan
#Email: senthilkumarl@live.com


import subprocess
from glob import glob



files=glob('*.eps')

print files

for f in files:
	f1,f2=f,f.split('.', 1 )[0]+'.jpg'
	print f1,'-->', f2
	result = subprocess.check_call(['convert', '-density', '300',f1,f2])

