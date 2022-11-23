

    
''''
problem_01: Create a laptop class with attributes like brand name,model name,price 
create two two objects/instance of your laptop.

Solution:
class Laptop:
    
    def __init__(self, brand_name,model_name,price):
        
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        
l1 = Laptop('Hp','11thgeration',150000)
l2 = Laptop('Lenovo','A12',144000)

print(l1.brand_name,l1.model_name,'=',l1.price)
print(l2.brand_name,l2.model_name,'=',l2.price) 

problem_02(Instance_methods related):  Findout discount price of any products using class

solution:
class Mobile:
    
    def __init__(self,brand_name,model_name,price):
        
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
       
        
    def apply_discount(self,num):
        
        offer_price = (num/100)*self.price
        
        return self.price - offer_price
    
    
mobile1 = Mobile('Realme','a54',40000)
mobile2 = Mobile('Oppo','A13',60000)

print(mobile1.apply_discount(10))     


problem_03: count instance or object in your class 

'''

class Sim:
    
    count_instance = 0
    
    def __init__(self,company_name,sim_quality,price):
        
        self.company_name = company_name
        self.sim_quality = sim_quality
        self.price = price
        Sim.count_instance+=1
    


s1 = Sim('Robi','4G',120)
s2 = Sim('Grameenphone','5G',150)

print(Sim.count_instance)    
    
       
    



            
        
      




       
        
     
    
