class Bankpage:

    def __init__(self):
        self.__balance = 0

    def show_balance(self, flag):
        if flag:
            print("You are allowed to see balance and balance is :-> ", self.__balance)

        else:
            print("Not allowed to view balance")

    def auth_user_balance(self, status):
        if status:
            self.show_balance(True)
        else:
            print("Not auth user")


jp_chase = Bankpage()
# jp_chase.show_balance(True)
jp_chase.auth_user_balance(True)


