#armstrong
n=int(input())
temp=n
r=0
while(n>0):
    
    remainder=n%10
    r=r*10+remainder
    sum=r*r*r
    n=n//10
if sum==n:
    print(armstrong)
else:
    print('not armstrong')

