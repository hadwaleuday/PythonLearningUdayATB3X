# Problem  Find the Max between 3 numbers

num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
num3 = int(input("Enter the third number\n"))

if num1>=num2 and num1>=num3:
    print("Number1 is greater")
elif num2>=num1 and num2>=num3:
    print("Number2 is greater")
else:
    print("Number3 is greater")