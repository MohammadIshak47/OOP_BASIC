## Property ,setter decorator

class Phone:
    
    def __init__(self,brand_name,model_name,price):
        
        self.brand_name = brand_name
        self.model_name = model_name
        #self._price = price
        '''if price>0:
            return self._pirce = price
        else:
            return self._price = 0
            '''
        self._price = max(price,0) # another way to avoid negative value    
        #self.complete_specification = f"{self.brand_name} {self.model_name} and {self._price}"
    
    @property
    def complete_specification(self):
        return f"{self.brand_name} {self.model_name} and price is {self._price}"
    @property
    def price(self):
        return self._price 
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number} ...")
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    
phone1 = Phone('Oppo','A12',14300)
phone2 = Phone('Samsung','S21ultra',23000)

#print(phone1.brand_name)
#print(phone1.model_name)
#print(phone1._price) 

#phone1._price = 10000 # to change value
#phone1._price = -100200 # Here we cant see that negative phone price is updated . Phone price never negative value
# We can solve this negative value problem ..
#print(phone1._price) # Here we can see that phone price  is updated 
#print(phone1.complete_specification)  #but in complete_specifiction phone price is not updated     

phone1.price =  12999
print(phone1.price)
#print(phone1.complete_specification())
print(phone1.complete_specification)          
        
        
        
      