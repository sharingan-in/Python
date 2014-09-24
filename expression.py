# python program to evaluate expressions eg: 2+4*5-6/2 the output will be 17
t=input()
t=int(t)

while t :
    print()
    k=input().split()
    
    i=1
    while k[i]!='=' :
        
        if k[i] == '+' :
            
            k[i+1]=int(k[i+1]) + int(k[i-1])
        
        
        elif k[i] == '-' :
        
            k[i+1]=int(k[i-1]) -int(k[i+1])
        elif k[i] == '*' :
            k[i+1]=int(int(k[i+1] )*int(k[i-1]))
        elif k[i] == '/' :
            k[i+1]=int(int(k[i-1]) /int(k[i+1]))
        

        i=i+2
    

    print(k[i-1])
    t=t-1


    
    
    
    
    
