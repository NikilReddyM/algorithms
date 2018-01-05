import math
for _ in range(int(input())):
    i,j = map(int,input().split())
    print(math.floor(math.sqrt(j))-math.ceil(math.sqrt(i))+1)