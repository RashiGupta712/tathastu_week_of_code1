import math 
def checkoddeven(n):
    if n%2!=0:
        print('input number is odd',end="")
    else:
        print('input number is even',end="")

def check_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    max_divisor=math.floor(math.sqrt(n))
    for i in range(3,1+int(max_divisor),2):
        if n%i==0:
            return False
    return True

def checkpalindrome(n):
    b=n
    rev = 0
    while(b > 0): 
        a = b % 10
        rev = rev * 10 + a 
        b = b // 10
    if rev==n:
        print(',palindrome',end="")

def checkarmstrong(n):
    sum = 0  
    temp = n  
  
    while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10
    if n==sum:
        print(',armstrong',end="")

n=int(input())
checkoddeven(n)
if check_prime(n):
    print("prime",end=" ")
checkpalindrome(n)
checkarmstrong(n)
