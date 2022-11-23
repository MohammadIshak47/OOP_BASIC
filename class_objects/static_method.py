## Static method ,have no relation in class or instance/object.
#but it has logical connection with class

class Person:
    
    count_instance = 0
    
    def __init__(self,first_name,last_name,age):
        
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
    @staticmethod
    def hello():
        print('Hello , static method')
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
p1 = Person('Ishak','Ahmed',26)
p2 = Person.from_string('Ishak,Ahmed,26')
print(p2.full_name())  

Person.hello()          
       