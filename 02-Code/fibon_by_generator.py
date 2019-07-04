def gen_fibbon(n):

    a=1
    b=1
    for i in range(n): 
        yield a
        a,b = b,a+b


for num in gen_fibbon(10):
    print(num)
#----------------

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
