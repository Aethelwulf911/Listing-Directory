import os,sys
def R(d):
	for i in os.listdir(d): 
		i=d+"/"+i
		if os.path.isdir(i):
			R(i),print(i)
		else:
			print(i)
R(sys.argv[1])