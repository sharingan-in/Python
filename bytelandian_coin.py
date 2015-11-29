coin={0:0,}
def change(n) :
    try :
        ans=coin[n]
    except :
        
        ans=0
        
    if ans :
        
        return int(ans)
    
    
    
    sums=int(n/2 )+ int(n/3) +int(n/4)
    if sums>n :
        ans= change(n/2) + change(n/3) + change(n/4)
        coin[n]=ans
        return int(ans)
    ans=n
    coin[n]=ans
    
    return int(ans)
t=10
while t :
    try :
        n=int(raw_input())
        
    except :
        break
    p=change(n)
    #print(len(coin))
    print(p)
    t=t-1
 
