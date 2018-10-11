
import math

def tolist():
    cases = int(input())
    for i in range(cases):
        case = input()
        edgelen = int(math.sqrt(len(case)))
        square = []
        for i in range(edgelen):
            row = []
            for j in range(edgelen):
                row.append(case[j + i * edgelen])
            square.append(row)
        # at this point square is a 2d list of input
        rev = revert(square)
        printFinal(rev)

def revert(l):
    edgelen = len(l)
    rev = []
    for i in range(len(l)-1, -1, -1): #col
        row = [] 
        for j in range(len(l)): #row
            row.append(l[j][i])
        rev.append(row)
    return rev

def printFinal(l):

    ans = ""
    for i in range(len(l)):
        for j in range(len(l)):
            ans += l[i][j]
    print(ans)

tolist()
