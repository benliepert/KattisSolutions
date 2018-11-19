

def b():
	i = input()
	i2= input()
	
	i2L = i2.split()
	i2L = [int(i) for i in i2L]
	
	count = 0
	s = 0
	for v in i2L:
		if v != -1:
			count += 1
			s += v
	print(s*1.0 / count)



b()
