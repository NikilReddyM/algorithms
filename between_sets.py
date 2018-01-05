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

def betweenTwoSets(a,b):
    x=lcm_list(a)
    y=gcd_list(b)
    if(x>y):
        print(0)
    else:
        count = 0
        for i in range(x,y+1,x):
            if(y%i==0 and i%x==0):
                count+= 1
        print(count)
            
t=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
betweenTwoSets(a,b)
