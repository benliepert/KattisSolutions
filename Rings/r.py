

def rings():
	i = input().split()
	rc = [int(e) for e in i]
	rows = rc[0]
	cols = rc[1]
	grid = []
	for i in range(rows):
		rStr = input()
		row = [c for c in rStr]
		grid.append(row)
	
	nums =[]
	for i in range(max(rows,cols)):
		grid,rn = markRing(grid,i+1)
		nums.append(rn)
	numRings = max(nums)
	dot =''
	if(numRings < 10):
		dot = '.'
	else:
		dot = '..'
	for row in grid:
		rs =""
		for col in row:
			rs = rs + dot + str(col)
		print(rs)
		
	
def markRing(L,ringNum):
	top = False
	bottom = False
	topRow = []
	bottomRow = []
	
	#mark top
	for i,row in enumerate(L):
		for j,col in enumerate(row):
			if col == 'T' and (j not in topRow):
				L[i][j] = ringNum
				topRow.append(j)
				top = True
	#mark bottom
	for r in range(len(L)-1,-1,-1):
		for j,col in enumerate(L[r]):
			if col == 'T' and (j not in bottomRow):
				L[r][j] = ringNum
				bottomRow.append(j)
				bottom = True
	#mark mid
	nums = [i for i in range(1,101,1)]
	for i,row in enumerate(L):
		firstEdge = False
		lastEdge = False
		for j,col in enumerate(row):
			if not firstEdge: # mark all Ts as ringNum
				if col == 'T' or col == ringNum:
					L[i][j] = ringNum
					firstEdge = True
			elif not lastEdge: #might have to iterate backwards for lastedge
				if col != 'T' and col != ringNum:
					L[i][j-1] = ringNum
					lastEdge = True
				elif j == len(row)-1:
					L[i][j] = ringNum
					lastEdge = True
	if(top or bottom):
		ringNum = ringNum
	else:
		ringNum = -1
	return L, ringNum
					
rings()