import math

def squarePeg():
	nums = input()
	nums = nums.split()
	N = int(nums[0])
	M = int(nums[1])
	K = int(nums[2])

	plotRadi = input()
	plotRadi = plotRadi.split()
	

	houseRadi = input()
	houseRadi = houseRadi.split()
	

	sides = input()
	sides = sides.split()
	

	plotRadi = list(map(int,plotRadi))
	houseRadi = list(map(int,houseRadi))
	sides = list(map(int,sides))

	sides.sort()
	houseRadi.sort()
	plotRadi.sort()

	fits = 0

	#print(plotRadi)
	#print(houseRadi)
	#print(sides)

	
	# for house in houseRadi:
	# 	p = fitCirc(house, plotRadi)
	# 	if p != -1:
	# 		houseRadi.remove(house)
	# 		plotRadi.remove(p)
	# 		fits += 1
	# 		#print("CIRC Match, Radius: {}, Plot: {}".format(house,p))
	# for side in sides:
	# 	p = fitSq(side, plotRadi)
	# 	if p != -1:
	# 		sides.remove(side)
	# 		plotRadi.remove(p)
	# 		fits += 1
	# 		#print("SQ Match, Radius: {}, Plot: {}".format(side,p))

	for plot in plotRadi:
		cFit = fc(plot,houseRadi)
		sFit = fsq(plot,sides)
		if cFit != -1 and sFit != -1:
			# pick best of both
			radC = cFit
			radS = math.sqrt(sFit**2 + sFit**2) / 2
			if radC > radS:
				houseRadi.remove(cFit)
				#plotRadi.remove(plot)
				# print("CIRC Match, Radius: {}, Plot: {}".format(cFit,plot))
			elif radS > radC:
				sides.remove(sFit)
				#plotRadi.remove(plot)
				# print("SQUARE Match, Radius: {}, Plot: {}".format(sFit,plot))
			else:
				#shouldn't matter
				houseRadi.remove(cFit)
				#plotRadi.remove(plot)
				# print("SPECIAL CASE")
			fits += 1
		elif cFit != -1:
			houseRadi.remove(cFit)
			#plotRadi.remove(plot)
			fits += 1
			#print("CIRC Match, Radius: {}, Plot: {}".format(cFit,plot))
		elif sFit != -1:
			sides.remove(sFit)
			#plotRadi.remove(plot)
			fits += 1
			# print("SQUARE Match, Radius: {}, Plot: {}".format(sFit,plot))


	return fits

def fsq(plot,sides):
	for i in range(len(sides)-1,-1,-1):
		if plot > math.sqrt(sides[i]**2 + sides[i]**2) / 2: #there's space
				return sides[i]
	return -1

def fc(plot, houseRadi):
	for i in range(len(houseRadi)-1,-1,-1):
		if plot > houseRadi[i]:
			return houseRadi[i]
	return -1

def fitSq(sideLen, plots):
	for i in range(len(plots)):
		if plots[i] > math.sqrt(sideLen**2 + sideLen**2): #there's space
			return plots[i]
	return -1
			
	

def fitCirc(houseRad,plots):
	for i in range(len(plots)):
		if plots[i] > houseRad: #fits
			return plots[i]
	return -1
	

print(squarePeg())
