class Employee:
    def __init__(self,fname,lname,salary,bonus):
        self.fname = fname
        self.lname =lname
        self.salary = salary
        self.bonus = bonus
        
        
irfan = Employee('irfan','ahmed',30000,12000) 
abdullah = Employee('abullah','alhuzaifa',40000,17000)


print(irfan.fname,irfan.lname,irfan.bonus,irfan.salary)
print(abdullah.fname,abdullah.lname,abdullah.salary,abdullah.bonus)
       
      
        