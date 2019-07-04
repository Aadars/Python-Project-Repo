print('your welcome in the mall')
print('what you want to buy.')
print('press 1 if you want fruit material')
print('press 2 if you want toys')
print('press 3 if you want mobile phone')
n=int(input("enter the choice wht you want. i'll show you the way "))
if n==1:
    fruit={'apple':'40 rs/kg','banana':'50 rs/12p','mango':'80 rs/kg'}
    print('we have apple banana and mango to view the rate of fruit press 1 for apple,2 for banana,3 for mango')
    a=int(input('select the item what you want'))
    if a==1:
        k=fruit['apple']
        print(k)
    elif a==2:
        m=fruit['banana']
        print(m)
    elif a==3:
        l=fruit['mango']
        print(l)
    else:
        print("oops! sorry we don't have this food")
