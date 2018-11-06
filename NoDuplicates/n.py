	
def n():
	s = input()

	L = s.split()

	for word in L:
		if L.count(word) > 1:
			print("no")
			return
	print("yes")

n()
