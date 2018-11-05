

fields = input().strip().split()
nums = input().strip().split()
nums = [int(i)-20 for i in nums]
numInts = int(fields[0])
price = int(fields[1])

start = -1
OPT = []
n = len(nums)
for i in range(n-1,-1,-1):
    if i == n-1:
        OPT.append(max(0,nums[i]))
    else:
        OPT.append(max(0,nums[i]+OPT[start]))
    start += 1
print(max(OPT))
