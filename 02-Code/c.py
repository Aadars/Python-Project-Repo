def aada(a,b):
    return a+b
c=aada(1,2)
print(c)

a=input('enter value: ')
b=''
c='_'
for i in range(len(a)):
    b=a[-(i+1):]
    b=(c*((len(a)-1)-i)+b)
    print(b)    
print(aada(1,2))


