def beautifulDays(i,j,k):
    count = 0
    for x in range(i,j+1):
        t=list(str(x))
        t.reverse()
        if abs(x-int(''.join(t)))%k ==0:
            count += 1
    return count

i,j,k = map(int,input().split())
print(beautifulDays(i,j,k))