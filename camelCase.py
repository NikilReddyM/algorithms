x=list(input())
print(len(list(filter(lambda x : ord(x) < 97,x)))+1)