# Encapsulation -
# bind the data variables with the methods
# Data Member - / Class Variables
# Methods - Def function within the class
# Wrapping or binding the data variables with the methods - Encapsulation.

# Hide the data members(class variables, instance variables) by using only the methods.
# In this programme password can be changed hence it is not good example.

class Car:
    username = "CarUser"
    password = "123"
    
    def __init__(self):
        print("I am called when object is created")

    def change_password(self):
        password = "345"


xuv = Car()
xuv.password="678"
new_password= xuv.password
print(new_password)

