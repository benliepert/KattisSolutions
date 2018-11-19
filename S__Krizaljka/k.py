words = input().strip().split()
A = words[0]
B = words[1]

N = len(A)
M = len(B)

picked = ""
for letter in A:
	if letter in B:
		picked = letter
		break

Ai = A.find(picked)
Bi = B.find(picked)

out = ""
for i in range(M):
	if i == Bi:
		row = A
	
	else:
		row = '.'*Ai
		row += B[i]
		row += '.'*(N-Ai-1)
	out += row + '\n'


print(out)
