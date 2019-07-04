def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

a=int(input("enter the 1st no."))
b=int(input("enter the 2nd no."))

print("please choice what you want to do")
print("for addition press 1")
print("for substraction press 2")
print("for multipication press 3")
print("for division press 4")
n=int(input("enter the choice"))

if n== 1:
    print(a,'+',b,'=',add(a,b))
elif n == 2:
    print(a,'-',b,'=',sub(a,b))
elif n == 3:
    print(a,'*',b,'=',mul(a,b))
elif n==4:
    print(a,'/',b,'=',div(a,b))
else:
    print('invalid input')
    
