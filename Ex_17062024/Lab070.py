#Factorial Programme

number = int(input("Enter the number:\t"))
factorial = 1
#Using while loop
# while number > 0:
#     factorial = factorial*number
#     number = number -1


#Using for loop
for i in range(1,number+1):
    # factorial = factorial*number
    factorial *= i
    number = number-1


print("Factorial of given number is: ", factorial)

