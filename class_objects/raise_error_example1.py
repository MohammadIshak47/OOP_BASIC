# raise error
# Not implement error
# Abstract method

class Animal:
    
    def __init__(self,name):
        self.name = name
    
    def sound(self):
        raise NotImplementedError('Please define this method in subclasses.') 

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)  
        self.breed = breed
    def sound(self):
        return 'ghew ghew'    

class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name) 
        self.breed = breed
        
    def sound(self):
        return 'mew mew'
        
dog = Dog('dog','ghew ghew')   
print(dog.sound()) 
cat = Cat('')                 
        