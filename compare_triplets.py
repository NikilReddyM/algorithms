def compareTriplet(ar,br):
    a=0
    b=0
    for i in range(3):
        if ar[i]>br[i]:
            a += 1
        if ar[i]<br[i]:
            b += 1
    return(a,b)


ar = list(map(int,input().strip().split()))
br = list(map(int,input().strip().split()))
a,b = compareTriplet(ar,br)
print(a,b)