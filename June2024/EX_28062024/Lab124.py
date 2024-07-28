class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def __init__(self):
        print("default car model default constructor")

    def car_vehicle(self):
        print("Selected car is of name:--> ",self.name)
        print("Selected car is of model:--> ",self.model)
        print("Selected car is of name:--> ",self.make)


car_a = Car("Harrier", "TATA", "SUV")
car_a.car_vehicle()
car_b = Car()
