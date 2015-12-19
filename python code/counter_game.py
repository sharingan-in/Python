t=int(input())
while t :
    
    c=0
    n=int(input())
    while n>1 :
        
        if(n and not(n&(n-1))) :
            u=0
            while n!=1 :
                n=n>>1
                u=u+1
            c=c+u
            break
        else :
            k=n
            
            
            k=int(k)
            i=0
            while pow(2,i)<n :
                k=pow(2,i)
                i=i+1
              
            n=n-k
            
            c=c+1
         
    t=t-1
    if c==0 : print('Louise')
    elif c%2!=0 :
        print('Louise')
    else :
        print('Richard')
    
    
