#program to check if the number is power of 2
t=int(input())

while t :
    m=int(input())
    j=1
    
    if m != 0 and ((m & (m - 1)) == 0) :
        print('yes')
    	
        
    else :
        print('NO')
        
    t=t-1
    
    

