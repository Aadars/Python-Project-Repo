def ask():
    while True:
        try:
            n=int(input("Enter the Number : "))
            
        except:
            if n == '':
                print('null')
            print('an error occured! Please try again!')

        else:
            result = n**2
            print(result)
        finally:
            print('always run')
        
ask()
