
# Multiple inheritance


class A:
     
     def class_a_method(self):
         return 'I am just a class A method'
     
     def hello(self):
         return 'Hello from class A'
class B:
    
    def class_b_method(self):
        return 'I am just a class B method'
    def hello(self):
        return 'Hello from class B'

#class C(A,B):# it will first call A and will print it.
class C(B,A): # it will first call B and will print it. 
    
    pass

instance_c = C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())

print(instance_c.hello()) # it will first call A and will print it. 
# print(help(C)) # To check method resolution order(MRO)
#print(C.mro()) # To check method resolution order(MRO)
print(C.__mro__) # To check method resolution order(MRO)
             