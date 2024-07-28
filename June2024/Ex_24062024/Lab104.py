# Filter in Python
# The filter() function in Python is a built-in function
# allows you to filter elements in the list, tuple, set.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_nums(n):
    return n % 2 == 0


#filter require arguments first is function for filteration i.e criteria
#and second argument entity of elements
new_number = filter(even_nums, numbers)
print("Even numbers in given list of numbers: ", list(new_number))


def five_nums(n):
    return n > 5


new_numbers = filter(five_nums, numbers)
print(list(new_numbers))

