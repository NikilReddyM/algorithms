from itertools import product

def getMoneySpent(keyboards, drives, s):
    max = -1
    for a,b in list(product(keyboards, drives)):
        if a+b <= s and a+b > max:
            max = a+b
    return max
    

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
