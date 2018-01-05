def findDigits(a):
    b=int(a)
    c=0
    for i in a:
        if int(i) == 0:
            continue
        c += int(b%int(i) == 0)
    return c


for _ in range(int(input())):
    print(findDigits(input()))