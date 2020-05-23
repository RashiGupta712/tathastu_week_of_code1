a=int(input("Enter the value"))
n=0
for i in range(a,-1,-1):
    print(i*"*"+" "*n+"*"*i)
    n+=2
n-=4
for i in range(1,a+1):
    print("*"*i+" "*n+"*"*i)
    n-=2
