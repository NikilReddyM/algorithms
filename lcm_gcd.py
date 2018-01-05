def gcd(M,N):
    m=max(M,N)
    n=min(M,N)
    while(n != 0):
        r=m%n
        m=n
        n=r
    return m

def gcd_rec(m,n):
    if(n):
        return gcd_rec(n,m%n)
    else:
        return m
    
def lcm(m,n):
    return (m*n)//gcd_rec(m,n)

def gcd_list(a):
    g=0
    for i in a:
        g=gcd_rec(i,g)
    return g

def lcm_list(a):
    l=1
    for i in a:
        l=lcm(i,l)
    return l

