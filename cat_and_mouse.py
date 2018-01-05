#!/bin/python3

def catAndMouse(x,y,z):
    if(abs(x-z)> abs(y-z)):
        print("Cat B")
    elif(abs(x-z) < abs(y-z)):
        print("Cat A")
    else:
        print("Mouse C")
            
q = int(input().strip())
for _ in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    catAndMouse(x,y,z)
