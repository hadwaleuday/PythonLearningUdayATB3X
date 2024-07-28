# Sum Of digits

def sum_digit(num):
    # Base Case
    if num<10 :
        return num

    # Recursive Case
    else:
        return num%10 + sum_digit(num//10)


print(sum_digit(1234))

#-- / gives floating number division
#-- // gives integer number division
