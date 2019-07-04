def square_num(n):

    for i in range(n):

        yield(i**2)

print(list(square_num(10)))

    
