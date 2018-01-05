n=int(input())
x=list(map(int,input().split()))
d,m = map(int,input().split())
c=0
for i in range(n-m+1):
    k=x[i:i+m]
    if sum(k)==d:
        c += 1
print(c)