def drawingBook(n,p):
    f=p//2
    b= n//2-f
    if f<b:
        return f
    return b

n=int(input())
p=int(input())
print(drawingBook(n,p))