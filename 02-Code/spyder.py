print('do you want to play gambling')
print('for yes enter 1 otherwise enter 2')
n=int(input('enter the choice. '))
if n==1:
    print('choose your Number between from 0 to 10')
    s=int(input('enter the no between 0 to 10 for playing the game'))
    from random import randint
    a= randint(0,1)
    if s==a:
        print('you win')
    else:
        print('sorry you losse the game')
else:
    print('Thankyou')
