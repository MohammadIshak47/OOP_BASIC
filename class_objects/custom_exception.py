

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name)<8:
        raise NameTooShortError('name is too short')
    
       

username = input('Please enter your name :')
username(validate)
       
print(f'hello {username}')        
    


# 
    