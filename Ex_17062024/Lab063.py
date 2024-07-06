# *args - any number of arguments
def print_arguments(*args):
    for numbers in args:
        print(numbers)


#Passing numbers
print_arguments(1, 2, 3, 4)

#Passing Strings
print_arguments("uday", "rau", "Dada")

#Passing srings and numbers 
print_arguments(1, "Dada", 2, "Rau")

