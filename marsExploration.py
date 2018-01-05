x=input()
c=0
for i in range(0,len(x),3):
   c += int(not x[i] == 'S') + int(not x[i+1] == 'O') + int(not x[i+2] == 'S')
print(c)