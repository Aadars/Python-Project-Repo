from functools import reduce
def mul(a,b):

    return a+b
nums=[1,1,2,3,4]
c=reduce(mul,nums)
print(c)
