from collections import Counter
n=int(input())
x= input().split()
print(n-Counter(x).most_common(1)[0][1])