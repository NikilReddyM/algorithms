def bon_appetite(cost,k,charged):
    if sum(cost)/2 == charged:
        return cost[k]//2
    return "Bon Appetit"

n,k = map(int,input().split())
cost = list(map(int,input().split()))
charged = int(input())
print(bon_appetite(cost,k,charged))