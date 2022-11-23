class Employee:
    
    increment = 1.5
    no_of_employees = 0
    def __init__(self,fname,lname,salary,bonus):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.bonus = bonus
        Employee.no_of_employees+=1
        
        
    def increase(self):
        self.salary = int(self.salary*self.increment )  

jubayer = Employee('jubayer','ahmed',450000,30000)
# sauda = Employee('sauda','chowdhury',330000,20000)


print(jubayer.salary)
jubayer.increase()
print(jubayer.salary)
print(Employee.no_of_employees)


# print(jubayer.fname,jubayer.salary)   

     
        
       
    