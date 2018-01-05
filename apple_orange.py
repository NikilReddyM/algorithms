s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
x=list(map(int,input().split()))
o=list(map(int,input().split()))
c=0
for d in x:
    if a+d in range(s,t+1):
        c += 1
print(c)
c=0
for d in o:
    if b+d in range(s,t+1):
        c += 1
print(c)
