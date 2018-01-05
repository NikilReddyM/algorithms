def matrix(n):
    m=[]
    for _ in range(n):
        m.append(list(map(int,input().strip().split())))
    return m

def diagnolDiff(m,n):
    l=0
    r=0
    for i in range(n):
        l += m[i][i]
        r += m[i][n-1-i]
    return(abs(l-r))

n=int(input())
m = matrix(n)
result = diagnolDiff(m,n)
print(result)