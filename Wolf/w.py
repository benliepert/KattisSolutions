
cards = []
n1 = int(input())
for i in range(n):
	c = input().strip().split()
	cards.append(c)

n2 = 52 - n1

if n2 > n1:
	print("impossible")

elif n2 < n1:
	#make first n2 not match your first n2 cards
	# could beat them on the last card or not, doesn't matter

else:
	#equal #, make first n2-1 cards not match your first n2-1 cards,
	#	last card must match and yours must be higher suit
	# if can't find card of same suit in which yours is higher, impossible
	# right off the bat
