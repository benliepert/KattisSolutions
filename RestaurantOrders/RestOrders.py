def buildOPT(items):
    # we need to output the INDICES of the items that are used,
    #   not the items themselves.

    # need values to denote ambiguous or impossible

    # need to extend range of this list because each item can cost up to 1000
    OPT = [-1 for i in range(31000)] # initialize everything to impossible (-1) at first
    OPT[0] = 0
    for i in range(len(items)): # for all items
        curOrder = items[i] # cost of current item
        for j in range(30001): # for all possible order values
            if OPT[j] >= 0: # not impossible
                if OPT[j+curOrder] == -1: # if the opt when item is included is impossible
                    OPT[j+curOrder] = i
                else:
                    OPT[j+curOrder] = -2 # it had something besides impossible there, aka its ambiguous
            elif OPT[j] == -2: # if current thing is ambiguous
                OPT[j+curOrder] = -2 # then the next sum that uses this is also ambiguous

    return OPT

def solve(OPT,items,order):
    # this function just handles proper output based on a single
    # order, it doesn't return anything (only prints)
    if OPT[order] == -1:
        print("Impossible")
    elif OPT[order] == -2:
        print("Ambiguous")
    else:
        answer = []
        while(order > 0): #rebuild the solution like we talked about in class
            answer.append(OPT[order] + 1) # need to offset by 1 because the first thing should be the 1st not 0th
            order -= items[OPT[order]] # we just included the order, so we subtract it off
        answer.reverse() # answer is backwards because we built it top down
        ansString = ""
        for i in range(len(answer)-1):
            ansString += str(answer[i]) + " "
        ansString += str(answer[len(answer)-1])
        print(ansString)
def main():
    numItems = int(input())
    items = [int(i) for i in input().strip().split()]
    numOrders = int(input())
    orders = [int(i) for i in input().strip().split()]

    # we can build the OPT table first, then simply call a function
    # to use it an output the correct thing (solve)
    OPT = buildOPT(items)
    
    for order in orders:
        solve(OPT,items,order) 
main()