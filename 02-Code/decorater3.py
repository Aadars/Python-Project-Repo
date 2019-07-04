def deco_mul(func):
    def inner(a,b,c):
        return a*b*c
    return inner


@deco_mul
def mul(a,b):
    return a*b
print(mul(2,3,5))



##---------------------------other code --------------------------------##

def sam_
