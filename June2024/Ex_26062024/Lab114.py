class Person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # Behaviour
    def talk(self):
        print("I can talk")

    def sleep(self, name):
        print("I am in sleep method")
        print(name, " is sleeping")

    def sleep2(self, name):
        print("I am in sleep2 Method")
        return None

    def talk_return(self):
        return "I am talking"


# Create Object of the Person Class
# objectRef = Object ->  ClassName()
Rohit = Person()
Rohit.name = "Rohit Sharma"
Rohit.talk()
Rohit.talk_return()
Rohit.sleep("Captain")

ritika = Person()
ritika.name = "Ritika Gupta"
ritika.talk()
