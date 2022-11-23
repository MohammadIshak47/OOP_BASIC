'''
# class variables
#Example_01

class Circle:
    pi = 3.1416
    
    def __init__(self,radius):
        self.radius =radius
        
    def circle_circumference(self):
        return 2*Circle.pi*self.radius
    
    
circle1 = Circle(5)
circle2 = Circle(7)

print(circle1.circle_circumference())  

#Class variable (Example_02)
# if all same discount offer 
class Headphone:
    
    discount_percent = 15 # class varibale = discount
    
    def __init__(self,brand_name,model_name,price):
        
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        
    def apply_discount(self):
        offer_price = (Headphone.discount_percent/100)*self.price
        return self.price - offer_price
    
h1 = Headphone('Hp','r44',5000)
h2 = Headphone('Asus','tt33',8900)

print(h1.apply_discount())  


'''


#Class variable (Example_03)
# if all different  discount offer  

class Headphone:
    discount_percent = 15
    
    def __init__(self,brand_name,model_name,price):
        
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        
    def apply_discount(self):
        #offer_price = (Headphone.discount_percent/100) * self.price 
        '''
       first it looking it on function variable,it can't this ,after that will looking for 
       class varible ,if match it, it will taken this and run 
        
        '''  
        offer_pirce = (self.discount_percent/100)*self.price
        return self.price - offer_pirce
    
h1 = Headphone('Dell','hrr33',78000)
h2 = Headphone('Asus','a88',99900)
h1.discount_percent = 10 # if we change now the discount_percent ,it will work.
print(h1.apply_discount())    
        
        
        
        
      



            
        
     

          