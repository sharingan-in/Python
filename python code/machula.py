# evalutes the expression and find and replaces the value for machula
#for eg : 12 + machula = 32 the output will be 12 + 20 = 32
j=input()
j=int(j)
print()
while j :
    
    
   
    
    a,b,c,d,e=input().split()
    
    #print(a,c,e,sep='\n')

    if 'machula' in a :
        #a=int(a)
        c=int(c)
        e=int(e)
        t=e-c
        a=t
        
        
    elif 'machula' in c  :
        
        
        a=int(a)
        #c=int(c)
        e=int(e)
        t=e-a
        c=t
        
    elif 'machula' in e :
    
        a=int(a)
        c=int(c)
        #e=int(e)
        t=a+c
        e=t


    print(a,b,c,d,e ,sep=' ')
    print()
    j=j-1

input()
    
