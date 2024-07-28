def decorator1(funcpara):
    def wrapper1():
        print("**BeforeDecorator1**")
        funcpara()
        print("**AfterDecorator1**")
    return wrapper1


def decorator2(funcpara2):
    def wrapper2(): #TypeError: 'NoneType' object is not callable
        print("**BeforeDecorator2**")
        funcpara2()
        print("**AfterDecorator2**")
    return wrapper2

@decorator1
@decorator2
def say_hello():
    print("Say Hello to all")


say_hello()

