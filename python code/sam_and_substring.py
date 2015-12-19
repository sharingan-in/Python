n=long(raw_input())

remd=1
sums=0
n1=n
c=0
while remd>0:
    c=0
    while n1>=1 :
        sums=long(sums+n1)
        n1=long(n1/10)
        c=c+1;
    #print(c,end='\n')
    remd=c-1
    if remd==0 :
        break
    p=pow(10,remd)
    #print(p,end='\n')
    n1=n%p

sums=int(sums%1000000007)
print(int(sums))
