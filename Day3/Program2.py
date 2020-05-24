a=list(map(int,input().split(',')))
b=list(map(int,input().split(',')))
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)    
