class Phone: # base class/parent class
    
    def __init__(self,brand_name,model_name,price):
        
        self.brand_name = brand_name
        self.model_name = model_name
        self._price = max(price,0)
        
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    def make_a_call(self,phone_number):
        print(f"calling {phone_number} ...")
        
class SmartPhone(Phone):
    
    def __init__(self, brand_name, model_name, price,ram,internal_memory,front_camera):
        super().__init__(brand_name, model_name, price) 
        
        self.ram = ram
        self.internal_memory = internal_memory
        self.front_camera = front_camera
    

phone = Phone('Nokia','1100',1200)
smartphone = SmartPhone('Samsung','s21ultra',140000,'6GB','64GB','48MEGAPIXEL') 

print(phone.full_name())
print(smartphone.full_name())
print(smartphone.full_name() + f" and price is {smartphone._price}")                  
        
 