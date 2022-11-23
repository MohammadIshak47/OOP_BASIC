class Person:
    
    
    def __init__(self,first_name,last_name,age,gender,nationality,bonus,income):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.bonus = bonus
        self.income = income
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"  
    
    def is_age_over_18(self):
        if self.age>18:
            print('You are a citizen of Bangladesh')
        else:
            print('You are not a citizen of Bangladesh')
            
    def total_income(self):
        
        total_amount = self.income + self.bonus
        
        return total_amount
        
         
        
       
        
                    
        
        
        
        
        
name1 = Person('Ishak','Ahmed',26,'male','Bangladeshi by birth',2000,25000) 

name2 = Person('Faisal','Imtiaz',14,'male','Pakistani',6000,30000) 


print(name1.full_name())
print(name1.first_name,name1.last_name,name1.age,name1.gender,name1.nationality)
print(name1.is_age_over_18()) 
print(name1.total_income())     
        
        