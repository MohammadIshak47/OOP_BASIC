'''
problem_01: make a function divide . divide(a,b) .print(divide(4,2)) 
,print(divide(4,0))#raise error please don't divide by zero.
print(divide('4',2)) # raise error please input numbers only .



'''

#solution :

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except:
        print('unexpected error !!!')        
        
print(divide(4,0) ) 
print(divide('4',3))

    