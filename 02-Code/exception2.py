def func():

    try:
        num1 = int(input('enter the 1st no. ')) 
        num2 = int(input('enter the 2nd no. '))
    
        result = num1/num2

        print(result)
       
    except ZeroDivisionError:
        print('00ps! is zero division error! ')
    finally:
        print('All Done!')

func()
