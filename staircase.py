def staircase(n):
    for i in range(n):
        print(' '*(n-1-i)+'#'*(i+1))

n=int(input())
staircase(n)