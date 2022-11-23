##Class method as constructor as constructor 


class Person:
    
    count_instance = 0
    
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def from_string(cls,string):
        first,last, age = string.split(',') 
        return cls(first,last,age)
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def is_age_over_18(self):
        return self.age>18

p1 = Person('Ishak','Ahmed',26)
p2 = Person('Rasel','Ahmed',16)

p3 = Person.from_string('Ishak,Ahmed,26') # Nijer icchemoto object create kora
p4 = Person.from_string('Rasel,Ahmed,16')

print(p3.full_name())  # Akhon object k call kora 
print(p4.full_name())    
       