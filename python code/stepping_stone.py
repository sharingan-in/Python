import math
t=int(input())
while t :
    n=int(input())*8 +1
    n=math.sqrt(n)
    if (n-1)%2==0 :
        print('Go On Bob',int((n-1)/2))
    else :
        print('Better Luck Next Time')
         
    
    t=t-1
