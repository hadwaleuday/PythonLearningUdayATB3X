class Vwologin:

    def __init__(self, email, password, name):
        self.__email = email
        self.name = name
        self.__password = password
        self.__name = name


    def confirm_login(self):
        if self.__email == "abc@hotmail.com" and self.__password == "123":
            print("Allowed to login")
        else:
            print("Not allowed")


page1 = Vwologin("abc@hotmail.com","123","uday")
print(page1.name)
#print(page1.__email)
page1.confirm_login()
# page1.__email = "??"
# page1.__password = "??"
