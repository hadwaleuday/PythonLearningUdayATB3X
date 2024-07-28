# Recursion
# Recursion is a programming technique where a function
# calls itself in order to solve a problem.

# Key Concepts
# 1. Base Case
# 2. Recursive Case

# Factorial
def factorial(num):
    # Base Case:
    if num == 0 or num == 1:
        return 1
    # Recursive Case
    else:
        return num * factorial(num-1)


print(factorial(5))