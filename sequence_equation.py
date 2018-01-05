a=['x']
n=int(input())
a.extend(list(map(int,input().split())))
for i in range(1,n+1):
    print(a.index(a.index(i)))