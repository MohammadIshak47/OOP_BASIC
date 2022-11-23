# We can derive more than one class from parent class/base class
# Multilavel inheritance 
# Method Resolution Order(MRO)
# Method overriding 
# isintance(), issubclass()

class Phone:
    
    def __init__(self,brand_name,model_name,price):
        
        self.brand_name = brand_name
        self.model_name = model_name
        self._price = price
        
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}...")

class SmartPhone(Phone):
    def __init__(self, brand_name, model_name, price,ram,front_camera):
        super().__init__(brand_name,model_name,price)
        
        self.ram = ram
        self.front_camera = front_camera
    def full_name(self):
        return f"{self.brand_name} {self.model_name} and price is {self._price}" # by using full_name here
    # Phone class ar full_name method ti overriding kora hoyeche (MR)    

class FlagShipPhone(SmartPhone): # it is called multilaveled inheritance . 
    def __init__(self, brand_name, model_name, price, ram, front_camera,back_camera,memory):
        super().__init__(brand_name, model_name, price, ram, front_camera)
        
        self.back_camera = back_camera
        self.memory = memory
        


smartphone = SmartPhone('Samsung','s21plus',21000,'4GB','16MP')
flagshipphone = FlagShipPhone('OPPO','E34',89999,'6GB','32MP','64MP','500GB')        

print(smartphone.full_name())
# print(help(SmartPhone))  # help function ti check korbe MRO Means full_name SmartPhone or Phone class ache ki na             
print(help(FlagShipPhone)) # akhon first check korbe full_name FlagShipPhone class a ache ki na then SmartPhone class check then Phone .jodi Phone class a pai then call korbe                   

print(isinstance(smartphone,SmartPhone))# by using isinstance function we can findout 
# smartphone object ti SmartPhone class ar ki na
print(issubclass(SmartPhone,Phone))
#using issubclass we can find SmartPhone class ti Phone class ar sub class ki na        
        