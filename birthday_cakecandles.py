def cakeCandlesBlown(a):
    return a.count(max(a))
    
n=input()
a=list(map(int,input().split()))
print(cakeCandlesBlown(a))