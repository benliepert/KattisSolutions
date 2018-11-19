def e():
	fields = input().strip().split()
	fields1 = input().strip().split()
	
	N = int(fields[0])
	M = int(fields[1])

	data = sorted(fields1)
	data = [int(i) for i in data]
	
	threshold = data[-1]
	
	collected = 0
	chosen = []

	while collected < M and threshold > 0:
		threshold -= 1		
		while len(data) > 0 and data[-1] > threshold:
			chosen.append(data[-1])
			data = data[:-1]
		collected = sum([int(i-threshold) for i in chosen])
		print("?", chosen)		
		print(collected, "---", threshold)
	print("dsa",threshold)
	 

e()
