# Question asked by students
# you can practice

sum = 0
num = int(input("Enter the number to find sum of its digits:\t"))
while num > 0:
    sum = sum + num%10
    num = num //10


print(sum)
