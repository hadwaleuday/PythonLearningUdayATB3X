class Dog:
    name = None
    breed = None

    def __init__(self,name,breed):
        self.name= name
        self.breed= breed

    def sleep(self):
        print("This one is sleeping:--> ", self.name)


#This way will not work without arguments
# dog1 = Dog()
# dog1.name= "Simba"
# dog1.sleep()
dog1 = Dog("Simba","Lion")
dog2 = Dog("Bagira","Black Panther")
dog1.sleep()
dog2.sleep()

print(f'{dog1.name} is of breed {dog1.breed}')
print(f'{dog2.name} is of breed {dog2.breed}')
