def plusMinus(m):
    p=0
    n=0
    for i in m:
        if i>0:
            p += 1
        if i<0:
            n+= 1
    return(p,n)


c=int(input())
m=list(map(int,input().strip().split()))
p,n = plusMinus(m)
print("%.6f"%(p/c))
print("%.6f"%(n/c))
print("%.6f"%((c-(p+n))/c))