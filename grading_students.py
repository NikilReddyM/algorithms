def grading(n):
    for _ in range(n):
        x= int(input())
        if x>37 and x%5>2:
            print(x+5-(x%5))
        else:
            print(x)
        
grading(int(input()))

