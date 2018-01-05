def valleys(steps):
    h=0
    vs = False
    vc=0
    for i in steps:
    
        if(h==0 and i=='D'):
            vs=True
    
        if(i=='U'):
            h += 1
        else:
            h -= 1
        if(h==0 and vs == True):
            vc += 1
            vs = False
    return(vc)

n=input()
print(valleys(input()))

