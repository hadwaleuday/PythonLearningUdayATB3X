# Function Scope

def my_function():
    a = 10
    local_var = 34
    print("Hello")
    print(a)


# print(a) # name 'a' is not defined/
# as a is defined in my_function() only, its scope is limited to that function only
my_function()
