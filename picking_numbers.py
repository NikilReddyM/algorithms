from itertools import combinations_with_replacement
def pickingNumbers(x):
    max = 0
    for a,b in list(combinations_with_replacement(set(x),2)):
        if abs(a-b)==1 and x.count(a)+x.count(b)>max:
            max = x.count(a)+x.count(b)
        if abs(a-b)==0 and x.count(a)>max:
            max = x.count(a)
    return(max)
n=input()
x=list(map(int,input().split()))
print(pickingNumbers(x))