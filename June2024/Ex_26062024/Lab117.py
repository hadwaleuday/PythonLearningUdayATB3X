class Dog:
    name = None
    id = None

    def __init__(self):
        print("Default No Argument")

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def sleep(self):
        print("sleeping")


dog1 = Dog("Chow","1")
#As here parameterized constructor presenr,
# Default constructor will not called by this
dog2 = Dog()
# print(dog1.name)
# print(dog1.id)
