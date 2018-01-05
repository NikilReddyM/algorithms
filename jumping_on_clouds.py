n,k = map(int,input().split())
a=input().split()
c=100
for i in range(0,n,k):
    c = c-(1+2*int(a[i]))
print(c)