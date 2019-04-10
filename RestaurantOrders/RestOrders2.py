def computeOPT(items,orderVal): 
    numItems = len(items)
    OPT = [[False for i in range(orderVal+1)] for i in range(numItems+1)] 

    for i in range(numItems+1): 
        # deal with base cases
        OPT[i][0] = True
        for k in range(1,orderVal+1): 
            OPT[0][k]=False
              
        for i in range(1,numItems+1): 
            for j in range(1,orderVal+1): 
                # use new opt to allow repeats
                if j<items[i-1]: 
                    OPT[i][j] = OPT[i-1][j] 
                if j>=items[i-1]: 
                    OPT[i][j] = (OPT[i-1][j] or OPT[i][j-items[i-1]]) # need this new OPT for repeats
    return OPT 

def findOPT(i,w,OPT,items):
    # print(i,w)
    if w == 0:
        print(i)
        return
    if i == 0 and w != 0:
        return
    # print(OPT[i-1][w])
    # print(OPT[i][w-items[i]])
    if OPT[i-1][w]:
        findOPT(i-1,w,OPT,items)
    if OPT[i][w-items[i]]:
        findOPT(i-1,w-items[i],OPT,items)
    
    

def count(items, orderVal):

    counts = [0 for i in range(orderVal+1)]
    counts[0] = 1 # base case, there's only one way to create 0 sum
    for item in items: # for every item
        for total in range(0, orderVal - item + 1): # for all valid order totals given the current item
            counts[total + item] += counts[total] # we know total + item is valid b/c range

    return counts[orderVal]

def main():
    numItems = int(input())
    items = [int(i) for i in input().strip().split()]
    numOrders = int(input())
    orders = [int(i) for i in input().strip().split()]

    for orderVal in orders:
        numWays = count(items, orderVal)
        if numWays == 0:
            print("Impossible")
        elif numWays >= 2: 
            print("Ambiguous")
        else:
            OPT = computeOPT(items,orderVal)
            # for row in OPT:
            #     print(row)
            # findOPT(len(items)-1,orderVal,OPT,items)
            findOPT(len(items)-1,orderVal,OPT,items)
        # use opt to build back solution

main()