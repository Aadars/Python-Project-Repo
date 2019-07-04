a=input('enter value: ')
b=''
c='_'
for i in range(len(a)):
    b=a[-(i+1):]
    b=(c*((len(a)-1)-i)+b)
    
    print(b)    
    
