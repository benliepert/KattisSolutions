def buildOPT(items, order):
    # we need to output the INDICES of the items that are used,
    #   not the items themselves.
    OPT = []

    return OPT

def solve(OPT,items,order):
    # this function just handles proper output based on a single
    # order, it doesn't return anything (only prints)

def main():
    numItems = int(input())
    items = [int(i) for i in input().strip().split()]
    numOrders = int(input())
    orders = [int(i) for i in input().strip().split()]

    # we can build the OPT table first, then simply call a function
    # to use it an output the correct thing
    OPT = buildOPT(items)
    
    for order in orders:
        solve(OPT,items,order) 
main()