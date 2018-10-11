def detailed():
    cases = int(input())
    for i in range(cases):
        A = input()
        B = input()
        print(A)
        print(B)
        ans = ""
        for i in range(len(A)):
            if A[i] == B[i]:
                ans += '.'
            else:
                ans += '*'
        print(ans)
        print()

detailed()