class Car:
    name = None

    def __init__(self):
        public_var = "Public"
        self._protected_var = "Protected123"
        self.__private_var = "Private@123"

    def __private_method(self):
        print("I am Private method")

    def printName(self):
        self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
        print("I am allowed public")



alto = Car()
alto.printName()
# alto.__private_var

# xuv = Car()
# xuv._Car__private_method()
# print(xuv._Car__private_var)