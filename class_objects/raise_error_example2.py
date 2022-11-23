class Mobile:
    
    def __init__(self,name):
        self.name = name

class MobileStore:
    
    def __init__(self):
        
        self.mobiles = []
    
    def add_mobile(self,new_mobile):
        
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new_mobile should be object of Mobile class')  
        



mobile = Mobile('Symphony')

samsung = 'samsung21s ultra'

mobilestore = MobileStore()

#mobilestore.add_mobile(samsung)
#print(mobilestore.add_mobile())

mobilestore.add_mobile(mobile)

mobile_phones = mobilestore.mobiles
print(mobile_phones[0].name)



       
          
                
              
      