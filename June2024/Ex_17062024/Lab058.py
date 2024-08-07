# Functions
# Block of Code - Which can executed or reused.
# Define
# Call

# Built Functions - bultins.py - file (Python 3 setup)
# Which are created by the Python Contributers
result = max(2, 3)


# User Defined
# They can return something
# The can't return -> non return
# They have parameters
# They don't parameters / arguments

# def say_hello():  # No Return Type and No Parameter / Argument
#     print("Hello")
#
#
# say_hello()
#
#
def say_hello_arg(name):  # No Return Type and with Argument
    print("Hello", name)


say_hello_arg("Uday")
say_hello_arg("Rau")


def say_hello_arg_default(name="Pramod sir"):  # No Return Type and with Default Argument
    # Write the Code
    print("Hello", name)


say_hello_arg_default()
say_hello_arg_default("Deeksha")
say_hello_arg_default(name="Sachin")


def sum_number_argument_ret(a, b): # Argument + return Type
    return a + b
