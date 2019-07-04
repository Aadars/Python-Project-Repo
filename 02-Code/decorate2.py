def deco_new(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
   

@deco_new
def div(a,b):
    return a/b
print(div(2,4))
