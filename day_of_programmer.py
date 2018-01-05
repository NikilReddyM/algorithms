def leap(x):
    if((x<1918 and x%4 == 0) or (x>1918 and (x%400 == 0 or (x%4 == 0 and x%100 != 0)))):
        return -1
    return 0

def solve(x):
    if x== 1918:
        return("26.09.1918")
    return str(13+leap(x))+".09."+str(x)

date = int(input())
result = solve(date)
print(result)
