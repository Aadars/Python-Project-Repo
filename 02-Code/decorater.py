def hello(name='Jose'):
    print('the hello() function has been executed')

    def greet():
        print('\tthis is the greet() function inside the hello')
    
    greet()
    print('its outside the function')
hello()

