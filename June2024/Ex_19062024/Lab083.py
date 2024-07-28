# Tuple - Collection of Items

my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list[0] = 21  # Mutable
print(my_list)
print(id(my_list))

my_tuple = (1, 2, 3, 4, 5, )
# my_tuple[0] = 21 # Immutable--TypeError: 'tuple' object does not support item assignment
print(my_tuple)
