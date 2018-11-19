
import math

def choose(n,r):
	return (math.factorial(n))/(math.factorial(r)*(math.factorial(n-r)))

def numDistincts(s):
	L = []
	for letter in s:
		if letter not in L:
			L.append(letter)
	return len(L)
	
def unique():
	numLetters = int(input())
	letters = input()
	numDistinct = numDistincts(letters)
	#print("Number of distinct letters = {}".format(numDistinct))
	numUnique = 0
	
	
	if numLetters == numDistinct:
		return math.factorial(numLetters)
		
	for i in range(numLetters-numDistinct+1):
		numUnique += (26-i)	* choose(numDistinct,numDistinct-i)
		#print("i = {}".format(i))
	
	return numUnique % (10**9 + 7)
	
print(int(unique()))