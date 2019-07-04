def str_upper(func):

    str1 = func()
    return str1.upper()

def print_str():
    return "good morning"

print(print_str())

d = str_upper(print_str)
print(d)


################ BUT the correct way to use Decorate in shown below ##########

def str_upper(func):

    str1 = func()
    return str1.upper()

@str_upper
def print_str():
    return "good morning"

print(print_str)
