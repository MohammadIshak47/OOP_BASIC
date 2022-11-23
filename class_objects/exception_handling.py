# Exception handling ( try except)
# try finally 

while True: # (it is infinite loop) by using it it will be continueoulsy raise error while take write input
 try:
  age = int(input("Enter your age : ")) # here can be raise error if we take string value
  break
 except ValueError:
    print('may be you entered string instead of numbers .try again ..')
 except: 
     print('unexpected error...')# here we know our error is value error . But we don' know the actual error then we have to use except  and our input ValueError may not right
if age > 18:
    print('You are a voter and you can  elected a member')
else:
    print('You aren\'t a voter & you can\'t elected a member')    