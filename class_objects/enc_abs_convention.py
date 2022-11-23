#Encapsulation
#Abstration
#Some special naming convention
# Name mangling 
# __name (this is not a convention)

class Phone:
    
    def __init__(self,brand_name,model_name,price):
        
        self.brand_name = brand_name
        self.model_name = model_name
        #self.price = price
        #self._price = price # _name # convention of private name
        self.__price = price #public not private                  # __name__# mane thunder/magic methods
    
    def make_a_phone_call(self,phone_number):
        print(f"calling {phone_number} ...")
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"  
    
phone1 = Phone('Samsung', 's21',15000)
phone2 = Phone('Realme','A12',12000)

#print(phone1._price) 

#phone1._price = -15000
#print(phone1._price) 
#print(phone1.__dict__)
#print(phone1.__price)

# print(phone1.__price)

print(phone1.__dict__)
print(phone1._Phone__price) # public not private

phone1._Phone__price = 16000 # To change the value
print(phone1._Phone__price)


    
           
        