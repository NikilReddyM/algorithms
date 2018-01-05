from collections import Counter
def sockMerchant(values):
    pairs = 0
    for i in Counter(values).values():
        pairs += i//2
    return pairs

n=input()
values = input().split()
print(sockMerchant(values))