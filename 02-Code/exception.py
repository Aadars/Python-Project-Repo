def func():

    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print('whoops! is type Error')
    else:
        print('All correct')
    finally:
        print('I always run whatever is condition')

func()
