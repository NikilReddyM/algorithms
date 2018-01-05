from itertools import combinations
def divisible_sumpairs(a,s):
    c=0
    for a,b in list(combinations(a,2)):
        if (a+b)%s == 0:
            c += 1
    return(c)
    

n,s = map(int,input().split())
a=map(int,input().split())
print(divisible_sumpairs(a,s))
