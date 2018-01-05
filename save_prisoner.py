def saveThePrisoner(n, m, s):
    # Complete this function
    x=(m+s-1)%n
    if x==0:
        return n
    return x

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
