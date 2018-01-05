def isClassConducted(n,k,a):
    a=list(filter(lambda x : x>0,a))
    return(['NO','YES'][n-len(a) < k])

for _ in range(int(input())):
    n,k = map(int,input().split())
    print(isClassConducted(n,k,list(map(int,input().split()))))