
def add(a,b):
    if (type(a) is int ) and (type(b) is int):
        return a+b
    
    raise TypeError('You are passing wrong data type')

print(add(2,'read'))