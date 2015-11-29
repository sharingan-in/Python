t=input()
t=int(t)
 
while t>0 :
    c=0
    a,b=raw_input().split()
    #b=input()
    n=int(a)
    a=list(a)
    b=int(b)
    while n<=b :
        k=list(str(n))
        a.reverse()
        if k==a :
            c=c+1
        n=n+1
        #print(a,k,sep=' ')
        a=list(str((n)))
        
        
    print(c)
    t=t-1
