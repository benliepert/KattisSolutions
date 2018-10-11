import math
n =  int(input())

mindays = n
for i in range(2,n):
	printers = 2**(i) #printers available
	days = math.ceil(n/printers + i)
	if days < mindays:
		mindays = days
		

print(mindays)
