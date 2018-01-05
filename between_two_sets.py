def betweenTwoSets(a,b):
    x=max(a)
    y=min(b)
    if(x>y):
        print(0)
    else:
        count = 0
        for i in range(x,y+1,x):
            c=0
            for j in a:    
                if i%j != 0:
                    c += 1
                    break
            for j in b:    
                if j%i != 0:
                    c += 1
                    break
            if(c==0):
                count+= 1
        print(count)
            
t=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
betweenTwoSets(a,b)

