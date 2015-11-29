t=input()
t=int(t)
while t :
    n=int(input())
    o=0
    e=0
    k=raw_input().split()
    i=0
    while i<n :
        if (int(k[i]))%2==0 :
            
            e=e+1
        else :
            o=o+1
        i=i+1
            
 
    n=n-1
    print(o*e)
    t=t-1
    
        
