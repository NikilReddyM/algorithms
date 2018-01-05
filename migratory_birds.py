from collections import Counter
n=input()
x=list(map(int,input().split()))
print(Counter(sorted(x)).most_common(1)[0][0])