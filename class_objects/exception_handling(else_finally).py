
while True:
    try:
        age = int(input('Enter your age : '))
    except ValueError:
        print('may be you entered string instead of numbers . please enter numbers')
    except:
        print('unexpected error ...')
    
    else:
        print(f'user input = {age}') # it show when no error,using it(else) we can increase readability and add extra code
        break  
    finally:
        print('finally blocks..') # error raise houk ba na houk always finally block print hoy  
    # we use finally block because we can show some information whatever our code execute or not 

if age > 18:
    print('You can play this game')
else:
    print('You can\'t play this game.')                
            